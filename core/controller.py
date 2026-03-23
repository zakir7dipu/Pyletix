import flet as ft

class BaseController:
    def __init__(self, page: ft.Page):
        self.page = page

    def render(self, view_content, title="Zak Flet App"):
        from core.router.response import Response
        return Response.view(view_content, title)

    def json(self, data):
        from core.router.response import Response
        return Response.json(data)

    def redirect(self, path):
        from core.router.response import Response
        return Response.redirect(path)
