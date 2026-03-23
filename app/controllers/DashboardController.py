from core.controller import BaseController
from core.auth.middleware import requires_auth
from app.views.layouts.main import MainLayout
from app.views.pages.dashboard import DashboardPage
from core.auth.auth_service import Auth

class DashboardController(BaseController):
    @requires_auth
    def index(self, request):
        user = Auth.user(self.page)
        user_name = user.name if user else "User"
        
        # Data for the page
        stats = {"users": 1500, "sessions": 45}
        
        # Render using Layout and Page
        view_content = DashboardPage.render(self.page, user_name=user_name, stats=stats)
        
        return self.render(
            view_content, 
            title="Dashboard - Pyletix", 
            layout=MainLayout
        )
