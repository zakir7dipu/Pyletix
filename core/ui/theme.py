import flet as ft

class ThemeManager:
    @staticmethod
    def toggle_theme(page: ft.Page):
        page.theme_mode = (
            ft.ThemeMode.DARK
            if page.theme_mode == ft.ThemeMode.LIGHT
            else ft.ThemeMode.LIGHT
        )
        page.update()

    @staticmethod
    def set_theme(page: ft.Page, mode: ft.ThemeMode):
        page.theme_mode = mode
        page.update()

    @staticmethod
    def get_colors(page: ft.Page):
        # Centralized color system based on theme
        is_dark = page.theme_mode == ft.ThemeMode.DARK
        return {
            "primary": "blue700",
            "secondary": "amber700",
            "background": "surface" if not is_dark else "black",
            "text": "onsurface" if not is_dark else "white",
        }
