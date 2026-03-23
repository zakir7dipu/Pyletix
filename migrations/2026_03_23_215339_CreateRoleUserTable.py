from core.database.schema import Schema

def up():
    Schema.create('role_user', lambda table: (
        table.integer('user_id'),
        table.integer('role_id')
    ))

def down():
    pass
