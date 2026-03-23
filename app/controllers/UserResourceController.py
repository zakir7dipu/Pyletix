from core.controller.resource_controller import ResourceController
from app.models.User import User
from core.auth.middleware import requires_jwt

class UserResourceController(ResourceController):
    model = User

    @requires_jwt
    def index(self, request):
        return super().index(request)

    @requires_jwt
    def show(self, request):
        return super().show(request)
