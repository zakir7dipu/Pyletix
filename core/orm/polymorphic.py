from .relationships import Relation

class MorphTo(Relation):
    def __init__(self, parent, name, type_col, id_col):
        super().__init__(parent, None)
        self.name = name
        self.type_col = type_col
        self.id_col = id_col

    def get_results(self):
        type_val = getattr(self.parent, self.type_col)
        id_val = getattr(self.parent, self.id_col)
        if not type_val or not id_val:
            return None
        
        # Dynamic import of related model based on type_val
        import importlib
        module_path = f"app.models.{type_val}"
        try:
            module = importlib.import_module(module_path)
            model_class = getattr(module, type_val)
            return model_class.find(id_val)
        except:
            return None

class MorphMany(Relation):
    def __init__(self, parent, related_model, type_col, id_col):
        super().__init__(parent, related_model)
        self.type_col = type_col
        self.id_col = id_col

    def get_results(self):
        parent_type = self.parent.__class__.__name__
        parent_id = getattr(self.parent, self.parent.primary_key)
        return self.query.where(self.type_col, parent_type).where(self.id_col, parent_id).get()
