from core.database.schema import Schema

def up():
    Schema.create('posts', lambda table: (
        table.id(),
        table.integer('user_id'),
        table.string('title'),
        table.string('content'),
        table.timestamps()
    ))

def down():
    Schema.drop('createpoststable')
