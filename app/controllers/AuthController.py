import flet as ft
from core.controller import BaseController
from core.auth.auth_service import Auth, Hash
from app.models.User import User

class AuthController(BaseController):
    def show_login(self):
        self.email_input = ft.TextField(label="Email")
        self.password_input = ft.TextField(label="Password", password=True, can_reveal_password=True)
        
        return self.render([
            ft.Text("Login", size=30),
            self.email_input,
            self.password_input,
            ft.ElevatedButton("Login", on_click=self.login),
            ft.TextButton("Register", on_click=lambda _: self.page.go("/register"))
        ])

    def login(self, e):
        user = User.where("email", self.email_input.value).first()
        if user and Hash.check(self.password_input.value, user.password):
            Auth.login(user, self.page)
            self.page.go("/")
        else:
            self.page.snack_bar = ft.SnackBar(ft.Text("Invalid credentials"))
            self.page.snack_bar.open = True
            self.page.update()

    def show_register(self):
        self.reg_name = ft.TextField(label="Name")
        self.reg_email = ft.TextField(label="Email")
        self.reg_pass = ft.TextField(label="Password", password=True)
        
        return self.render([
            ft.Text("Register", size=30),
            self.reg_name,
            self.reg_email,
            self.reg_pass,
            ft.ElevatedButton("Register", on_click=self.register)
        ])

    def register(self, e):
        hashed_pass = Hash.make(self.reg_pass.value)
        user = User.create(
            name=self.reg_name.value,
            email=self.reg_email.value,
            password=hashed_pass
        )
        Auth.login(user, self.page)
        self.page.go("/")

    def logout(self, e):
        Auth.logout(self.page)
        self.page.go("/login")
