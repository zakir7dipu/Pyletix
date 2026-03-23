import flet as ft
from app.views.components.hero import Hero
from app.views.components.card import Card
from app.views.components.button import FlexButton
from app.views.components.table import Table

class DashboardPage:
    @staticmethod
    def render(page: ft.Page, user_name="User", stats=None):
        if stats is None:
            stats = {"users": 124, "sessions": 12}

        hero = Hero(
            title=f"Welcome back, {user_name}!",
            subtitle="This is your new Pyletix Dashboard with clean architecture.",
            color="indigo700"
        )

        stats_cards = ft.ResponsiveRow([
            Card(
                title="Users",
                content=ft.Text(str(stats["users"]), size=30, weight="bold"),
                subtitle="Total registered users",
                col={"sm": 12, "md": 4}
            ),
            Card(
                title="Active Sessions",
                content=ft.Text(str(stats["sessions"]), size=30, weight="bold"),
                subtitle="Current online users",
                col={"sm": 12, "md": 4}
            ),
            Card(
                title="Revenue",
                content=ft.Text("$12,450", size=30, weight="bold"),
                subtitle="Last 30 days",
                col={"sm": 12, "md": 4}
            ),
        ], spacing=20)

        recent_activity = Card(
            title="Recent Activity",
            content=Table(
                columns=["User", "Action", "Date"],
                rows=[
                    ["John Doe", "Created Post", "2026-03-23"],
                    ["Jane Smith", "Updated Profile", "2026-03-22"],
                    ["Bob Wilson", "Deleted Post", "2026-03-21"],
                ]
            )
        )

        actions = ft.Row([
            FlexButton("Refresh Data", icon="refresh", variant="primary"),
            FlexButton("Export PDF", icon="picture_as_pdf", variant="outline"),
        ], spacing=10)

        return ft.Column([
            hero,
            stats_cards,
            ft.Container(height=20),
            recent_activity,
            ft.Container(height=20),
            actions,
        ], spacing=20)
