import flet as ft

class NotificationService:
    def __init__(self, page: ft.Page):
        self.page = page

    def toast(self, message, bgcolor=None):
        if bgcolor is None:
            bgcolor = "surfacevariant"
        self.page.snack_bar = ft.SnackBar(ft.Text(message), bgcolor=bgcolor)
        self.page.snack_bar.open = True
        self.page.update()

    def alert(self, title, message):
        def close_dlg(e):
            dlg_modal.open = False
            self.page.update()

        dlg_modal = ft.AlertDialog(
            modal=True,
            title=ft.Text(title),
            content=ft.Text(message),
            actions=[
                ft.TextButton("OK", on_click=close_dlg),
            ],
            actions_alignment="end",
        )
        self.page.dialog = dlg_modal
        dlg_modal.open = True
        self.page.update()

    def confirm(self, title, message, on_confirm):
        def handle_confirm(e):
            dlg_modal.open = False
            self.page.update()
            on_confirm()

        def handle_cancel(e):
            dlg_modal.open = False
            self.page.update()

        dlg_modal = ft.AlertDialog(
            modal=True,
            title=ft.Text(title),
            content=ft.Text(message),
            actions=[
                ft.TextButton("Cancel", on_click=handle_cancel),
                ft.TextButton("Confirm", on_click=handle_confirm),
            ],
            actions_alignment=ft.MainAxisAlignment.END,
        )
        self.page.dialog = dlg_modal
        dlg_modal.open = True
        self.page.update()
