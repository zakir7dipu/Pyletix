from core.database.schema import Schema

def up():
    Schema.create('permissions', lambda table: (
        table.id(),
        table.string('name'),
        table.string('slug'),
        table.timestamps()
    ))

def down():
    pass
