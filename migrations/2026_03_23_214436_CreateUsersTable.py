from core.database.schema import Schema

def up():
    Schema.create('users', lambda table: (
        table.id(),
        table.string('name'),
        table.string('email'),
        table.string('password'),
        table.timestamps()
    ))

def down():
    pass
