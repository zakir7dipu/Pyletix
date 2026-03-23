from core.controller import BaseController
from core.auth.auth_service import Auth, Hash
from app.models.User import User
from app.views.layouts.auth import AuthLayout
from app.views.pages.login import LoginPage
from app.views.pages.register import RegisterPage
from app.services.notification_service import NotificationService

class AuthController(BaseController):
    def index(self):
        # If logged in, go to dashboard, else go to login
        if Auth.check(self.page):
            return self.redirect("/dashboard")
        return self.redirect("/login")

    def show_login(self):
        view_content = LoginPage.render(
            self.page, 
            on_login=self.handle_login,
            on_register_click=lambda _: self.page.go("/register")
        )
        return self.render(view_content, title="Pyletix - Login", layout=AuthLayout)

    def handle_login(self, email, password):
        user = User.where("email", email).first()
        if user and Hash.check(password, user.password):
            Auth.login(user, self.page)
            self.page.go("/")
        else:
            NotificationService(self.page).toast("Invalid email or password")

    def show_register(self):
        view_content = RegisterPage.render(
            self.page,
            on_register=self.handle_register,
            on_login_click=lambda _: self.page.go("/login")
        )
        return self.render(view_content, title="Pyletix - Register", layout=AuthLayout)

    def handle_register(self, name, email, password):
        if not name or not email or not password:
            NotificationService(self.page).toast("Please fill all fields")
            return

        hashed_pass = Hash.make(password)
        user = User.create(
            name=name,
            email=email,
            password=hashed_pass
        )
        Auth.login(user, self.page)
        self.page.go("/")

    def logout(self, e=None):
        Auth.logout(self.page)
        self.page.go("/login")
