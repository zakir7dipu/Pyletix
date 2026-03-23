import sys
import os
import importlib
from core.database import db

# Reuse logic from flet-art.py but expand it
def create_model(name):
    path = f"app/models/{name}.py"
    content = f"""from core.orm.model import BaseModel

class {name}(BaseModel):
    table = '{name.lower()}s'
"""
    with open(path, "w") as f:
        f.write(content)
    print(f"Model {name} created.")

def create_controller(name):
    path = f"app/controllers/{name}.py"
    content = f"""import flet as ft
from core.controller import BaseController

class {name}(BaseController):
    def index(self, request):
        return self.render([ft.Text("Index of {name}")])
"""
    with open(path, "w") as f:
        f.write(content)
    print(f"Controller {name} created.")

def create_migration(name):
    import datetime
    timestamp = datetime.datetime.now().strftime("%Y_%m_%d_%H%M%S")
    filename = f"{timestamp}_{name}.py"
    path = f"migrations/{filename}"
    content = f"""from core.database.schema import Schema

def up():
    Schema.create('{name.lower()}', lambda table: (
        table.id(),
        table.timestamps()
    ))

def down():
    Schema.drop('{name.lower()}')
"""
    with open(path, "w") as f:
        f.write(content)
    print(f"Migration {filename} created.")

def create_module(name):
    create_model(name)
    create_controller(f"{name}Controller")
    create_migration(f"Create{name}sTable")

def migrate():
    # Reuse migration logic or call it
    os.system("python flet-art.py migrate")

def rollback():
    # Get last migration batch
    last_batch = db.fetch_one("SELECT MAX(batch) as batch FROM migrations")['batch']
    if not last_batch:
        print("Nothing to rollback.")
        return
    
    migrations = db.fetch_all("SELECT migration FROM migrations WHERE batch = ? ORDER BY id DESC", (last_batch,))
    for m in migrations:
        name = m['migration']
        print(f"Rolling back: {name}")
        # Import and call down()
        module = importlib.import_module(f"migrations.{name}")
        module.down()
        db.execute("DELETE FROM migrations WHERE migration = ?", (name,))
    print("Rollback complete.")

def seed():
    print("Running seeders...")
    # Logic to run DatabaseSeeder
    try:
        module = importlib.import_module("app.database.seeds.DatabaseSeeder")
        seeder = module.DatabaseSeeder()
        seeder.run()
        print("Seeding complete.")
    except Exception as e:
        print(f"Seeding failed: {e}")

def main():
    if len(sys.argv) < 2:
        print("Usage: python manage.py [command]")
        return

    command = sys.argv[1]
    
    if command == "make:model": create_model(sys.argv[2])
    elif command == "make:controller": create_controller(sys.argv[2])
    elif command == "make:migration": create_migration(sys.argv[2])
    elif command == "make:module": create_module(sys.argv[2])
    elif command == "migrate": migrate()
    elif command == "migrate:rollback": rollback()
    elif command == "db:seed": seed()
    else: print(f"Unknown command: {command}")

if __name__ == "__main__":
    main()
