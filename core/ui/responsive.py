import flet as ft

class Responsive:
    @staticmethod
    def is_mobile(page: ft.Page):
        return page.width < 600

    @staticmethod
    def is_tablet(page: ft.Page):
        return 600 <= page.width < 1000

    @staticmethod
    def is_desktop(page: ft.Page):
        return page.width >= 1000

    @staticmethod
    def get_device_type(page: ft.Page):
        if page.width < 600:
            return "mobile"
        elif page.width < 1000:
            return "tablet"
        else:
            return "desktop"
