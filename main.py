import flet as ft
from core.router.router import Router
from core.auth.auth_service import Auth

def main(page: ft.Page):
    page.title = "Zak Flet MVC"
    router = Router(page)
    
    # Register routes
    router.get("/login", "AuthController@show_login")
    router.get("/register", "AuthController@show_register")
    router.get("/logout", "AuthController@logout")
    router.get("/users", "UserController@index")
    router.get("/dashboard", "DashboardController@index")
    router.get("/posts", "PostController@index")
    router.get("/posts/create", "PostController@create")
    
    # API Routes
    router.prefix("/api/v1")
    router.get("/users", "UserResourceController@index")
    router.get("/users/:id", "UserResourceController@show")
    router.prefix("") # Reset prefix
    
    # Redirect if not logged in
    public_routes = ["/login", "/register"]
    if page.route not in public_routes and not Auth.check(page):
        page.go("/login")
        return

    # For initial app, we'll redirect to / dashboard if logged in
    if page.route == "/" or page.route == "" or page.route is None:
        if Auth.check(page):
            page.go("/dashboard")
        else:
            page.go("/login")
    
    page.update()

if __name__ == "__main__":
    ft.app(target=main)
