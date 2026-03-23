from core.database.schema import Schema

def up():
    Schema.create('permission_role', lambda table: (
        table.integer('permission_id'),
        table.integer('role_id')
    ))

def down():
    pass
