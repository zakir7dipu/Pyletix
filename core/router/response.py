import flet as ft
import json

class Response:
    def __init__(self, content=None, status=200):
        self.content = content
        self.status = status

    @classmethod
    def view(cls, controls, title=None, appbar=None):
        return cls(content={"type": "view", "controls": controls, "title": title, "appbar": appbar})

    @classmethod
    def json(cls, data):
        return cls(content={"type": "json", "data": data})

    @classmethod
    def redirect(cls, path):
        return cls(content={"type": "redirect", "path": path})
