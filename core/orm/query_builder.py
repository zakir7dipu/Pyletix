from ..database import db

class QueryBuilder:
    def __init__(self, table, model_class=None):
        self.table = table
        self.model_class = model_class
        self._columns = "*"
        self._where = []
        self._where_params = []
        self._joins = []
        self._group_by = None
        self._limit = None
        self._order_by = None
        self._eager_loads = []

    def with_(self, *relations):
        self._eager_loads.extend(relations)
        return self

    def select(self, *columns):
        self._columns = ", ".join(columns)
        return self

    def where(self, column, value, operator='='):
        if isinstance(value, list) or operator == "IN":
            placeholders = ", ".join(["?" for _ in value])
            self._where.append(f"{column} IN ({placeholders})")
            self._where_params.extend(value)
        else:
            self._where.append(f"{column} {operator} ?")
            self._where_params.append(value)
        return self

    def join(self, table, first, second, type='INNER'):
        self._joins.append(f"{type} JOIN {table} ON {first} = {second}")
        return self

    def group_by(self, column):
        self._group_by = column
        return self

    def limit(self, value):
        self._limit = value
        return self

    def order_by(self, column, direction='ASC'):
        self._order_by = f"{column} {direction}"
        return self

    def get(self):
        query = f"SELECT {self._columns} FROM {self.table}"
        for join in self._joins:
            query += f" {join}"
        if self._where:
            query += " WHERE " + " AND ".join(self._where)
        if self._group_by:
            query += f" GROUP BY {self._group_by}"
        if self._order_by:
            query += f" ORDER BY {self._order_by}"
        if self._limit:
            query += f" LIMIT {self._limit}"
        
        rows = db.fetch_all(query, self._where_params)
        
        if self.model_class:
            models = [self.model_class(**dict(row)) for row in rows]
            if self._eager_loads:
                from .eager_loader import EagerLoader
                models = EagerLoader.load(models, self._eager_loads)
            return models
        
        return rows

    def first(self):
        query = f"SELECT {self._columns} FROM {self.table}"
        for join in self._joins:
            query += f" {join}"
        if self._where:
            query += " WHERE " + " AND ".join(self._where)
        if self._group_by:
            query += f" GROUP BY {self._group_by}"
        if self._order_by:
            query += f" ORDER BY {self._order_by}"
        query += " LIMIT 1"
        
        row = db.fetch_one(query, self._where_params)
        if not row:
            return None

        if self.model_class:
            model = self.model_class(**dict(row))
            if self._eager_loads:
                from .eager_loader import EagerLoader
                EagerLoader.load([model], self._eager_loads)
            return model
            
        return row

    def insert(self, data):
        columns = ", ".join(data.keys())
        placeholders = ", ".join(["?" for _ in data])
        query = f"INSERT INTO {self.table} ({columns}) VALUES ({placeholders})"
        cursor = db.execute(query, list(data.values()))
        return cursor.lastrowid

    def update(self, data):
        set_clause = ", ".join([f"{col} = ?" for col in data])
        params = list(data.values())
        query = f"UPDATE {self.table} SET {set_clause}"
        if self._where:
            query += " WHERE " + " AND ".join(self._where)
            params.extend(self._where_params)
        
        db.execute(query, params)
        return True

    def delete(self):
        query = f"DELETE FROM {self.table}"
        if self._where:
            query += " WHERE " + " AND ".join(self._where)
        
        db.execute(query, self._where_params)
        return True
