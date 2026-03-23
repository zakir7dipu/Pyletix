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
        self.page.on_view_pop = self._handle_view_pop

    def _handle_view_pop(self, e):
        if len(self.page.views) > 1:
            self.page.views.pop()
            top_view = self.page.views[-1]
            self.page.go(top_view.route)
        else:
            # If only one view remains, don't pop (prevent black screen)
            pass

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
        
        # Avoid duplicate views for the same route during back/forward
        if self.page.views and self.page.views[-1].route == e.route:
            return

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
            return Response.view([ft.Container(content=ft.Text(f"System Error: {ex}", color="red"), padding=50)])

    def _handle_response(self, response):
        if not response: return

        if response.content["type"] == "view":
            appbar = response.content.get("appbar")
            if not appbar:
                appbar = ft.AppBar(
                    title=ft.Text(response.content.get("title", "Pyletix")),
                    bgcolor="surfacevariant"
                )
            
            # Stable view stack management with theme-awareness
            self.page.views = [ft.View(
                route=self.page.route,
                controls=response.content["controls"] if isinstance(response.content["controls"], list) else [response.content["controls"]],
                appbar=appbar,
                padding=20,
                bgcolor=None # Enable theme-aware backgrounds
            )]
        elif response.content["type"] == "redirect":
            self.page.push_route(response.content["path"])
        elif response.content["type"] == "json":
            self.page.views.append(ft.View(self.page.route, [ft.Text(json.dumps(response.content["data"]))]))
