from core.database import db

class Schema:
    @staticmethod
    def create(table_name, callback):
        blueprint = Blueprint(table_name)
        callback(blueprint)
        sql = blueprint.to_sql()
        db.execute(sql)
        print(f"Table {table_name} created successfully.")

    @staticmethod
    def table(table_name, callback):
        blueprint = Blueprint(table_name, mode='alter')
        callback(blueprint)
        for sql in blueprint.to_alter_sql():
            db.execute(sql)
        print(f"Table {table_name} altered successfully.")

class Blueprint:
    def __init__(self, table_name, mode='create'):
        self.table_name = table_name
        self.mode = mode
        self.columns = []

    def id(self):
        self.columns.append("id INTEGER PRIMARY KEY AUTOINCREMENT")
        return self

    def string(self, name):
        self.columns.append(f"{name} TEXT")
        return self

    def integer(self, name):
        self.columns.append(f"{name} INTEGER")
        return self

    def timestamps(self):
        self.columns.append("created_at DATETIME DEFAULT CURRENT_TIMESTAMP")
        self.columns.append("updated_at DATETIME DEFAULT CURRENT_TIMESTAMP")
        return self

    def to_sql(self):
        cols = ", ".join(self.columns)
        return f"CREATE TABLE IF NOT EXISTS {self.table_name} ({cols})"

    def to_alter_sql(self):
        # SQLite only supports adding one column at a time
        sqls = []
        for col in self.columns:
            sqls.append(f"ALTER TABLE {self.table_name} ADD COLUMN {col}")
        return sqls
