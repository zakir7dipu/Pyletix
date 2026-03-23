import flet as ft

class BaseLayout:
    def __init__(self, page: ft.Page):
        self.page = page

    def render(self, content):
        """Assembles the layout and returns a list of controls."""
        raise NotImplementedError("Layouts must implement the render method.")
