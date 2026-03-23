from core.orm.model import BaseModel

class Permission(BaseModel):
    table = 'permissions'

    def roles(self):
        return self.belongs_to_many('Role', 'permission_role')
