import flet as ft

class ValidationUI:
    @staticmethod
    def error_text(message):
        return ft.Text(message, color="red700", size=12)

    @staticmethod
    def highlight_error(control: ft.TextField, message):
        control.error_text = message
        control.update()

    @staticmethod
    def clear_error(control: ft.TextField):
        control.error_text = None
        control.update()
