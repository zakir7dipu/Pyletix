from core.orm.model import BaseModel

class User(BaseModel):
    table = 'users'

    def roles(self):
        from .Role import Role
        return self.belongs_to_many(Role, 'role_user')

    def has_role(self, role_slug):
        # Eager load roles if possible or just check
        roles = self.roles
        return any(r.slug == role_slug for r in roles)

    def has_permission(self, permission_slug):
        roles = self.query().with_('roles.permissions').find(self.id).roles
        for role in roles:
            if any(p.slug == permission_slug for p in role.permissions):
                return True
        return False
