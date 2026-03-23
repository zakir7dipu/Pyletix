from .query_builder import QueryBuilder

class Relation:
    def __init__(self, parent, related_model):
        self.parent = parent
        self.related_model = related_model
        self.query = related_model.query()

    def get_results(self):
        raise NotImplementedError

class HasOne(Relation):
    def __init__(self, parent, related_model, foreign_key, local_key):
        super().__init__(parent, related_model)
        self.foreign_key = foreign_key
        self.local_key = local_key

    def get_results(self):
        parent_value = getattr(self.parent, self.local_key)
        return self.query.where(self.foreign_key, parent_value).first()

class HasMany(Relation):
    def __init__(self, parent, related_model, foreign_key, local_key):
        super().__init__(parent, related_model)
        self.foreign_key = foreign_key
        self.local_key = local_key

    def get_results(self):
        parent_value = getattr(self.parent, self.local_key)
        return self.query.where(self.foreign_key, parent_value).get()

class BelongsTo(Relation):
    def __init__(self, parent, related_model, foreign_key, owner_key):
        super().__init__(parent, related_model)
        self.foreign_key = foreign_key
        self.owner_key = owner_key

    def get_results(self):
        parent_value = getattr(self.parent, self.foreign_key)
        return self.query.where(self.owner_key, parent_value).first()

class BelongsToMany(Relation):
    def __init__(self, parent, related_model, pivot, foreign_pivot_key, related_pivot_key):
        super().__init__(parent, related_model)
        self.pivot = pivot
        self.foreign_pivot_key = foreign_pivot_key
        self.related_pivot_key = related_pivot_key

    def get_results(self):
        parent_value = getattr(self.parent, self.parent.primary_key)
        related_table = self.related_model.table
        
        # JOIN pivot ON pivot.related_pivot_key = related.id
        # WHERE pivot.foreign_pivot_key = parent.id
        self.query.join(self.pivot, f"{self.pivot}.{self.related_pivot_key}", f"{related_table}.id")
        self.query.where(f"{self.pivot}.{self.foreign_pivot_key}", parent_value)
        
        return self.query.get()
