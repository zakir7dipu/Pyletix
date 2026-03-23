import flet as ft

class Card(ft.Container):
    def __init__(self, content, title=None, subtitle=None, actions=None, width=None, padding=20, **kwargs):
        controls = []
        if title:
            controls.append(ft.Text(title, size=20, weight="bold"))
        if subtitle:
            controls.append(ft.Text(subtitle, size=14, color="secondary"))
        
        if title or subtitle:
            controls.append(ft.Divider(height=20, thickness=1))
            
        if isinstance(content, list):
            controls.extend(content)
        else:
            controls.append(content)
            
        if actions:
            controls.append(ft.Divider(height=20, thickness=0.5))
            controls.append(ft.Row(actions, alignment="end"))
            
        super().__init__(
            content=ft.Column(controls, tight=True, horizontal_alignment="center"),
            padding=padding,
            border=ft.border.all(1, "outlinevariant"),
            border_radius=12,
            bgcolor="surface",
            shadow=ft.BoxShadow(
                spread_radius=1,
                blur_radius=5,
                color="black12",
                offset=ft.Offset(0, 2),
            ),
            width=width,
            **kwargs
        )
