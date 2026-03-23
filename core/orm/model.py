from .query_builder import QueryBuilder
from .relationships import HasOne, HasMany, BelongsTo, BelongsToMany
from .polymorphic import MorphTo, MorphMany
from ..database import db

class BaseModel:
    table = None
    primary_key = 'id'
    
    def __init__(self, **attributes):
        self._attributes = attributes
        for key, value in attributes.items():
            setattr(self, key, value)
        self._relationships = {}

    def __getattr__(self, name):
        # Check if it's an eager-loaded relationship
        cache_name = f"_{name}_cache"
        if hasattr(self, cache_name):
            return getattr(self, cache_name)
            
        # Allow dynamic access to relationship results (lazy loading)
        if name in self._relationships:
            return self._relationships[name].get_results()
        raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{name}'")

    @classmethod
    def query(cls):
        return QueryBuilder(cls.table, model_class=cls)

    @classmethod
    def all(cls):
        rows = cls.query().get()
        return [cls(**dict(row)) for row in rows]

    @classmethod
    def find(cls, id):
        row = cls.query().where(cls.primary_key, id).first()
        if row:
            return cls(**dict(row))
        return None

    @classmethod
    def where(cls, column, value, operator='='):
        return cls.query().where(column, value, operator)

    def has_one(self, related_model, foreign_key=None, local_key=None):
        foreign_key = foreign_key or f"{self.table[:-1]}_id"
        local_key = local_key or self.primary_key
        return HasOne(self, related_model, foreign_key, local_key)

    def has_many(self, related_model, foreign_key=None, local_key=None):
        foreign_key = foreign_key or f"{self.table[:-1]}_id"
        local_key = local_key or self.primary_key
        return HasMany(self, related_model, foreign_key, local_key)

    def belongs_to(self, related_model, foreign_key=None, owner_key=None):
        foreign_key = foreign_key or f"{related_model.table[:-1]}_id"
        owner_key = owner_key or related_model.primary_key
        return BelongsTo(self, related_model, foreign_key, owner_key)

    def belongs_to_many(self, related_model, pivot, foreign_pivot_key=None, related_pivot_key=None):
        foreign_pivot_key = foreign_pivot_key or f"{self.table[:-1]}_id"
        related_pivot_key = related_pivot_key or f"{related_model.table[:-1]}_id"
        return BelongsToMany(self, related_model, pivot, foreign_pivot_key, related_pivot_key)

    def morph_to(self, name=None, type_col=None, id_col=None):
        import inspect
        name = name or inspect.stack()[1][3]
        type_col = type_col or f"{name}_type"
        id_col = id_col or f"{name}_id"
        return MorphTo(self, name, type_col, id_col)

    def morph_many(self, related_model, name, type_col=None, id_col=None):
        type_col = type_col or f"{name}_type"
        id_col = id_col or f"{name}_id"
        return MorphMany(self, related_model, type_col, id_col)

    @classmethod
    def create(cls, **data):
        id = cls.query().insert(data)
        return cls.find(id)

    def save(self):
        data = self._attributes.copy()
        # Update attributes from object properties (in case they were changed)
        for key in data:
            if hasattr(self, key):
                data[key] = getattr(self, key)
        
        if hasattr(self, self.primary_key) and getattr(self, self.primary_key):
            id = getattr(self, self.primary_key)
            self.query().where(self.primary_key, id).update(data)
        else:
            id = self.query().insert(data)
            setattr(self, self.primary_key, id)
        return self

    def delete(self):
        if hasattr(self, self.primary_key) and getattr(self, self.primary_key):
            id = getattr(self, self.primary_key)
            self.query().where(self.primary_key, id).delete()
            return True
        return False

    def to_dict(self):
        return self._attributes
