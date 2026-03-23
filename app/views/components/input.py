import flet as ft

class Input(ft.TextField):
    def __init__(self, label, value="", placeholder="", password=False, icon=None, on_change=None, width=None, **kwargs):
        super().__init__(
            label=label,
            value=value,
            hint_text=placeholder,
            password=password,
            can_reveal_password=password,
            prefix_icon=icon,
            on_change=on_change,
            width=width,
            border_radius=8,
            border_color="outline",
            focused_border_color="blue700",
            content_padding=15,
            **kwargs
        )
