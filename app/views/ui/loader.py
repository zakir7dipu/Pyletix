import flet as ft

class Loader(ft.Stack):
    def __init__(self, message="Loading...", visible=False):
        self.message_text = ft.Text(message, color="white")
        self.progress_ring = ft.ProgressRing(width=40, height=40, stroke_width=4, color="blue700")
        
        container = ft.Container(
            content=ft.Column([
                self.progress_ring,
                self.message_text,
            ], alignment="center", horizontal_alignment="center"),
            bgcolor="black87",
            alignment="center",
            expand=True,
        )
        
        super().__init__(
            controls=[container],
            visible=visible,
            expand=True,
        )

    def show(self, message=None):
        if message:
            self.message_text.value = message
        self.visible = True
        self.update()

    def hide(self):
        self.visible = False
        self.update()
