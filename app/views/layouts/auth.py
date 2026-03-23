import flet as ft
from .base import BaseLayout

class AuthLayout(BaseLayout):
    def __init__(self, page: ft.Page, title="Pyletix - Login"):
        super().__init__(page)
        self.title = title

    def render(self, content):
        return [
            ft.Column(
                [content],
                alignment="center",
                horizontal_alignment="center",
                expand=True
            )
        ]
