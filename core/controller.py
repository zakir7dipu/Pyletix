import flet as ft

class BaseController:
    def __init__(self, page: ft.Page):
        self.page = page

    def render(self, view_content, title="Pyletix App", layout=None):
        from core.router.response import Response
        
        if layout:
            # If a layout class is passed, instantiate it
            if isinstance(layout, type):
                layout_instance = layout(self.page, title=title)
                view_content = layout_instance.render(view_content)
                # If the layout provides a header, we'll use it
                header = getattr(layout_instance, 'header', lambda: None)()
                return Response.view(view_content, title, appbar=header)
        
        return Response.view(view_content, title)

    def json(self, data):
        from core.router.response import Response
        return Response.json(data)

    def redirect(self, path):
        from core.router.response import Response
        return Response.redirect(path)
