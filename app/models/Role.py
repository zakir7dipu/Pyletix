from core.orm.model import BaseModel

class Role(BaseModel):
    table = 'roles'

    def permissions(self):
        return self.belongs_to_many('Permission', 'permission_role')
