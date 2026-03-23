import flet as ft

class Navbar(ft.AppBar):
    def __init__(self, title, actions=None, bgcolor="surfacevariant"):
        if actions is None:
            actions = []
            
        self.theme_icon = ft.IconButton(
            icon="dark_mode", # Default, will be updated
            on_click=lambda e: self._toggle_theme(e.page)
        )
        actions.append(self.theme_icon)

        super().__init__(
            title=ft.Text(title, weight="bold"),
            actions=actions,
            bgcolor=bgcolor,
            center_title=False,
            elevation=0,
        )

    def _toggle_theme(self, page):
        from app.services.theme_service import ThemeService
        ThemeService.toggle(page)
        # Dynamic icon update
        self.theme_icon.icon = "dark_mode" if page.theme_mode == "light" else "light_mode"
        page.update()
