import flet as ft
from core.controller import BaseController
from app.models.User import User

class UserController(BaseController):
    def index(self):
        # Fetch all users using ORM
        users = User.all()
        
        user_controls = []
        for user in users:
            user_controls.append(ft.ListTile(title=ft.Text(user.name)))

        return self.render([
            ft.Text("User List", size=25, weight=ft.FontWeight.BOLD),
            ft.Column(user_controls, scroll=ft.ScrollMode.AUTO),
            ft.ElevatedButton("Add Sample User", on_click=self.add_user)
        ])

    def add_user(self, e):
        import random
        names = ["Alice", "Bob", "Charlie", "Diana"]
        User.create(name=random.choice(names))
        self.page.go("/users")
