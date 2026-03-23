import flet as ft
from app.views.components.card import Card
from app.views.components.button import FlexButton
from app.views.components.input import Input

class RegisterPage:
    @staticmethod
    def render(page: ft.Page, on_register, on_login_click):
        name_input = Input(label="Full Name", icon="person")
        email_input = Input(label="Email Address", icon="email")
        password_input = Input(label="Password", password=True, icon="lock")
        
        register_button = FlexButton(
            "Create Account", 
            on_click=lambda _: on_register(name_input.value, email_input.value, password_input.value),
            width=320
        )

        content = ft.Column([
            ft.Text("Join Us", size=32, weight="bold"),
            ft.Text("Start building with Pyletix MVC", color="secondary"),
            ft.Container(height=20),
            name_input,
            email_input,
            password_input,
            ft.Container(height=10),
            register_button,
            ft.Row([
                ft.Text("Already have an account?"),
                ft.TextButton("Login here", on_click=on_login_click)
            ], alignment="center")
        ], horizontal_alignment="center")

        return Card(content=content, padding=30)
