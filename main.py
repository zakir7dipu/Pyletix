import flet as ft
from core.router.router import Router
from core.auth.auth_service import Auth
from routes import inside, api

def main(page: ft.Page):
    page.title = "Pyletix MVC"
    router = Router(page)
    
    # Load Routes
    inside.register(router)
    api.register(router)
    
    # Auth middleware (Global check)
    public_routes = ["/login", "/register"]
    if page.route not in public_routes and not Auth.check(page):
        page.go("/login")
        return

    if page.route == "/" or page.route == "" or page.route is None:
        if Auth.check(page):
            page.go("/dashboard")
        else:
            page.go("/login")
    
    page.update()

if __name__ == "__main__":
    ft.app(target=main)
