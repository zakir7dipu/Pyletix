import flet as ft
from core.controller import BaseController
from core.auth.middleware import requires_auth, requires_role
from app.views.components.base_ui import Hero, Card
from app.services.notification_service import NotificationService

class DashboardController(BaseController):
    @requires_auth
    def index(self, request):
        notifications = NotificationService(self.page)
        
        # Accessing request query params
        user_name = request.get_query("name", "User")
        
        hero = Hero(
            title=f"Welcome back, {user_name}!",
            subtitle="Explore your advanced Flet MVC Dashboard",
            color=ft.colors.INDIGO_700
        )
        
        stats_card = Card(
            title="Application Stats",
            content=[
                ft.Text("Total Users: 124"),
                ft.Text("Active Sessions: 12"),
                ft.ElevatedButton("Show Toast", on_click=lambda _: notifications.toast("Hello from Dashboard!"))
            ]
        )

        admin_action = ft.Container()
        # Simulated admin check (actual check would use has_role)
        from core.auth.auth_service import Auth
        user = Auth.user(self.page)
        if user and user.has_role("admin"):
            admin_action = ft.ElevatedButton("Admin Alert", on_click=lambda _: notifications.alert("Admin", "Sensitive Action!"))

        return self.render([
            hero,
            ft.Row([stats_card, Card(title="Quick Actions", content=[admin_action])]),
        ], title="Dashboard")
