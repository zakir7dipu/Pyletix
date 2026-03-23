import functools
import flet as ft
from .auth_service import Auth
from .jwt_service import JWTService
from core.router.response import Response

def requires_auth(func):
    @functools.wraps(func)
    def wrapper(self, *args, **kwargs):
        if not Auth.check(self.page):
            self.page.go("/login")
            return None
        return func(self, *args, **kwargs)
    return wrapper

def requires_jwt(func):
    @functools.wraps(func)
    def wrapper(self, request, *args, **kwargs):
        token = request.get_query("token")
        if not token:
            return Response.json({"error": "Token required"}, 401)
        
        payload = JWTService.validate(token)
        if not payload:
            return Response.json({"error": "Invalid or expired token"}, 401)
        
        request.user_id = payload['user_id']
        return func(self, request, *args, **kwargs)
    return wrapper

def requires_role(role_slug):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(self, *args, **kwargs):
            user = Auth.user(self.page)
            if not user or not user.has_role(role_slug):
                return ft.View(self.page.route, [ft.Text("Unauthorized: Role required")])
            return func(self, *args, **kwargs)
        return wrapper
    return decorator

def requires_permission(permission_slug):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(self, *args, **kwargs):
            user = Auth.user(self.page)
            if not user or not user.has_permission(permission_slug):
                return ft.View(self.page.route, [ft.Text("Unauthorized: Permission required")])
            return func(self, *args, **kwargs)
        return wrapper
    return decorator
