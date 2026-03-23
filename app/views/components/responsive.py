import flet as ft
from core.ui.responsive import Responsive

class ResponsiveComponent(ft.Container):
    """
    A base component that can change its content based on device type.
    """
    def __init__(self, mobile=None, tablet=None, desktop=None, **kwargs):
        super().__init__(**kwargs)
        self.mobile_content = mobile
        self.tablet_content = tablet
        self.desktop_content = desktop or tablet or mobile
        
    def build(self):
        device = Responsive.get_device_type(self.page)
        if device == "mobile":
            self.content = self.mobile_content
        elif device == "tablet":
            self.content = self.tablet_content or self.desktop_content
        else:
            self.content = self.desktop_content
