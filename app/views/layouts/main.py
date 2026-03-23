from .base import BaseLayout
from app.views.partials.header import Header
from app.views.partials.footer import Footer
from core.ui.responsive import Responsive
import flet as ft

class MainLayout(BaseLayout):
    def __init__(self, page: ft.Page, title="Pyletix App"):
        super().__init__(page)
        self.title = title

    def header(self):
        # Add menu button for mobile
        header = Header(self.page, title=self.title)
        if Responsive.is_mobile(self.page):
            header.leading = ft.IconButton(
                "menu", 
                on_click=lambda _: self.toggle_drawer()
            )
        return header

    def toggle_drawer(self):
        self.page.drawer.open = not self.page.drawer.open
        self.page.update()

    def sidebar(self):
        rail = ft.NavigationRail(
            selected_index=0,
            label_type=ft.NavigationRailLabelType.ALL,
            min_width=100,
            min_extended_width=200,
            extended=True,
            destinations=[
                ft.NavigationRailDestination(icon="dashboard", label="Dashboard"),
                ft.NavigationRailDestination(icon="post_add", label="Posts"),
                ft.NavigationRailDestination(icon="settings", label="Settings"),
            ],
        )
        return rail

    def render(self, content):
        is_mobile = Responsive.is_mobile(self.page)
        
        main_content = ft.Container(
            content=content if isinstance(content, ft.Control) else ft.Column(content, scroll=ft.ScrollMode.AUTO),
            expand=True,
            padding=20,
        )

        # Setup Drawer for mobile
        if is_mobile:
            self.page.drawer = ft.NavigationDrawer(
                controls=[
                    ft.NavigationDrawerDestination(icon="dashboard", label="Dashboard"),
                    ft.NavigationDrawerDestination(icon="post_add", label="Posts"),
                    ft.NavigationDrawerDestination(icon="settings", label="Settings"),
                ]
            )

        if is_mobile:
            # Mobile layout: No sidebar, drawer instead
            layout = ft.Column([main_content, Footer()], expand=True)
        else:
            # Desktop layout: Permanent sidebar
            layout = ft.Row(
                [
                    self.sidebar(),
                    ft.VerticalDivider(width=1, color="outlinevariant"),
                    ft.Column([main_content, Footer()], expand=True),
                ],
                expand=True,
            )

        return [layout]
