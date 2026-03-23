import flet as ft
from .request import Request
from .response import Response
import re
import json

class Router:
    def __init__(self, page: ft.Page):
        self.page = page
        self.routes = {"GET": {}, "POST": {}, "PUT": {}, "DELETE": {}}
        self.middlewares = []
        self._current_prefix = ""
        self.page.on_route_change = self._handle_route_change

    def get(self, path, handler):
        self._add_route("GET", path, handler)

    def post(self, path, handler):
        self._add_route("POST", path, handler)

    def prefix(self, prefix_str):
        self._current_prefix = prefix_str
        return self

    def use(self, middleware):
        self.middlewares.append(middleware)

    def _add_route(self, method, path, handler):
        full_path = self._current_prefix + path
        pattern = re.sub(r':(\w+)', r'(?P<\1>[^/]+)', full_path)
        self.routes[method][f"^{pattern}$"] = handler

    def _handle_route_change(self, e):
        path = e.route.split("?")[0]
        method = "GET" # Simulation
        
        handler = None
        params = {}
        
        for pattern, h in self.routes[method].items():
            match = re.match(pattern, path)
            if match:
                handler = h
                params = match.groupdict()
                break

        if not handler:
            self.page.views.append(ft.View(path, [ft.Text("404 Not Found")]))
        else:
            request = Request(self.page, params)
            response = self._run_pipeline(request, handler)
            self._handle_response(response)
        
        self.page.update()

    def _run_pipeline(self, request, handler):
        def final_handler(req):
            if isinstance(handler, str):
                return self._call_controller(handler, req)
            return handler(req)
        return final_handler(request)

    def _call_controller(self, action_str, request):
        controller_name, method_name = action_str.split('@')
        import importlib
        try:
            module = importlib.import_module(f"app.controllers.{controller_name}")
            controller_class = getattr(module, controller_name)
            controller_instance = controller_class(self.page)
            method = getattr(controller_instance, method_name)
            
            import inspect
            sig = inspect.signature(method)
            if 'request' in sig.parameters:
                return method(request)
            return method()
        except Exception as ex:
            import traceback
            traceback.print_exc()
            return Response.view([ft.Text(f"Error: {ex}")])

    def _handle_response(self, response):
        if not response: return

        if response.content["type"] == "view":
            self.page.views.append(ft.View(
                route=self.page.route,
                controls=response.content["controls"],
                appbar=ft.AppBar(title=ft.Text(response.content["title"] or "Zak Flet"))
            ))
        elif response.content["type"] == "redirect":
            self.page.go(response.content["path"])
        elif response.content["type"] == "json":
            self.page.views.append(ft.View(self.page.route, [ft.Text(json.dumps(response.content["data"]))]))
