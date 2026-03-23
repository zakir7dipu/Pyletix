import flet as ft
from core.router.router import Router
from core.auth.auth_service import Auth
from routes import inside, api
from app.services.theme_service import ThemeService

def main(page: ft.Page):
    page.title = "Pyletix Framework"
    ThemeService.load(page)
    page.padding = 0
    
    router = Router(page)
    
    # Load Routes
    inside.register(router)
    api.register(router)

    # Auth Guard / Public Routes
    public_routes = ["/login", "/register"]
    
    if page.route not in public_routes and not Auth.check(page):
        page.go("/login")
        return
    
    if page.route == "/" or page.route == "":
        if Auth.check(page):
            page.go("/dashboard")
        else:
            page.go("/login")

    # Initial route handling
    router._handle_route_change(ft.ControlEvent(target=page, name="route_change", data=page.route))

    def on_resize(e):
        pass

    page.on_resize = on_resize
    page.update()

if __name__ == "__main__":
    ft.app(target=main)
