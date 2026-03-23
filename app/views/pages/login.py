import flet as ft
from app.views.components.card import Card
from app.views.components.button import FlexButton
from app.views.components.input import Input

class LoginPage:
    @staticmethod
    def render(page: ft.Page, on_login, on_register_click):
        email_input = Input(label="Email Address", icon="email")
        password_input = Input(label="Password", password=True, icon="lock")
        
        login_button = FlexButton(
            "Sign In", 
            on_click=lambda _: on_login(email_input.value, password_input.value),
            width=320
        )

        content = ft.Column([
            ft.Text("Welcome Back", size=32, weight="bold", color="black"),
            ft.Text("Please enter your details", color="grey"),
            ft.Container(height=20),
            email_input,
            password_input,
            ft.Container(height=10),
            login_button,
            ft.Row([
                ft.Text("Don't have an account?", color="black"),
                ft.TextButton("Create one", on_click=on_register_click)
            ], alignment="center")
        ], horizontal_alignment="center", width=400)

        return Card(content=content, padding=40)
