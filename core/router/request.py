import flet as ft

class Request:
    def __init__(self, page: ft.Page, route_params=None):
        self.page = page
        self.params = route_params or {}
        self.query = self._parse_query(page.route)
        self.session = page.session
        self.user = None # Set by Auth middleware

    def _parse_query(self, route):
        if "?" not in route:
            return {}
        query_str = route.split("?")[1]
        import urllib.parse
        return urllib.parse.parse_qs(query_str)

    def input(self, key, default=None):
        return self.params.get(key, default)

    def get_query(self, key, default=None):
        val = self.query.get(key, default)
        if isinstance(val, list) and len(val) == 1:
            return val[0]
        return val

    def all(self):
        return {**self.params, **self.query}
