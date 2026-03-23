from core.controller import BaseController
from core.router.response import Response

class ResourceController(BaseController):
    model = None

    def index(self, request):
        return self.json([m.all() for m in self.model.all()])

    def show(self, request):
        obj = self.model.find(request.input('id'))
        if not obj:
            return Response.json({"error": "Not found"}, 404)
        return self.json(obj.all())

    def store(self, request):
        obj = self.model.create(**request.all())
        return self.json(obj.all())

    def update(self, request):
        obj = self.model.find(request.input('id'))
        if not obj:
            return Response.json({"error": "Not found"}, 404)
        obj.update(**request.all())
        return self.json(obj.all())

    def destroy(self, request):
        obj = self.model.find(request.input('id'))
        if not obj:
            return Response.json({"error": "Not found"}, 404)
        obj.delete()
        return self.json({"success": True})
