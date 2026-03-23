import flet as ft

class Modal(ft.AlertDialog):
    def __init__(self, title, content, actions=None, on_dismiss=None):
        def close_modal(e):
            self.open = False
            self.page.update()
            if on_dismiss:
                on_dismiss()

        default_actions = [ft.TextButton("Close", on_click=close_modal)]
        
        super().__init__(
            modal=True,
            title=ft.Text(title, weight="bold"),
            content=content if isinstance(content, ft.Control) else ft.Text(content),
            actions=actions or default_actions,
            actions_alignment="end",
            on_dismiss=on_dismiss,
        )

    def show(self, page: ft.Page):
        page.dialog = self
        self.open = True
        page.update()
