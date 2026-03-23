import flet as ft

class Hero(ft.Container):
    def __init__(self, title, subtitle, color=ft.colors.BLUE_700):
        super().__init__()
        self.content = ft.Column([
            ft.Text(title, size=40, weight=ft.FontWeight.BOLD, color=ft.colors.WHITE),
            ft.Text(subtitle, size=20, color=ft.colors.WHITE70),
        ])
        self.bgcolor = color
        self.padding = 40
        self.border_radius = 10
        self.margin = ft.margin.only(bottom=20)

class Card(ft.Container):
    def __init__(self, content, title=None):
        super().__init__()
        controls = []
        if title:
            controls.append(ft.Text(title, size=20, weight=ft.FontWeight.BOLD))
            controls.append(ft.Divider())
        
        if isinstance(content, list):
            controls.extend(content)
        else:
            controls.append(content)
            
        self.content = ft.Column(controls)
        self.padding = 20
        self.border = ft.border.all(1, ft.colors.OUTLINE_VARIANT)
        self.border_radius = 8
        self.bgcolor = ft.colors.SURFACE
