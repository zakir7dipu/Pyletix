from core.database.schema import Schema

def up():
    Schema.create('rate_limits', lambda table: (
        table.string('key'),
        table.integer('attempts'),
        table.integer('expires_at')
    ))

def down():
    pass
