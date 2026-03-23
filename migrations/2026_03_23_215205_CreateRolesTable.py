from core.database.schema import Schema

def up():
    Schema.create('roles', lambda table: (
        table.id(),
        table.string('name'),
        table.string('slug'),
        table.timestamps()
    ))

def down():
    pass
