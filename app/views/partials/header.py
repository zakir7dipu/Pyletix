import flet as ft
from core.ui.theme import ThemeManager

class Header(ft.AppBar):
    def __init__(self, page: ft.Page, title="Pyletix"):
        super().__init__(
            title=ft.Text(title, weight="bold"),
            center_title=False,
            bgcolor="surfacevariant",
            actions=[
                ft.IconButton(
                    "brightness_4", 
                    on_click=lambda _: ThemeManager.toggle_theme(page)
                ),
                ft.IconButton("notifications"),
                ft.CircleAvatar(
                    content=ft.Icon("person"),
                    radius=15,
                ),
                ft.Container(width=10),
            ]
        )
