import flet as ft

class Hero(ft.Container):
    def __init__(self, title, subtitle=None, color="blue700", **kwargs):
        super().__init__(
            content=ft.Column([
                ft.Text(title, size=40, weight="bold", color="white"),
                ft.Text(subtitle, size=18, color="white70") if subtitle else ft.Container(),
            ], spacing=10),
            padding=50,
            bgcolor=color,
            border_radius=15,
            margin=ft.margin.only(bottom=30),
            shadow=ft.BoxShadow(
                spread_radius=1,
                blur_radius=10,
                color="blue70033", # with opacity
                offset=ft.Offset(0, 4),
            ),
        )
