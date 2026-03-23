import flet as ft

class ThemeService:
    @staticmethod
    def toggle(page: ft.Page):
        if page.theme_mode == "light":
            page.theme_mode = "dark"
        else:
            page.theme_mode = "light"
        
        # Correct API for this Flet version
        page.session.store.set("theme_mode", page.theme_mode)
        page.update()

    @staticmethod
    def load(page: ft.Page):
        # Correct API for this Flet version
        theme = page.session.store.get("theme_mode")
        if theme:
            page.theme_mode = theme
        else:
            page.theme_mode = "light"
        # No page.update() here as main() will do it
