from core.orm.model import BaseModel

class Post(BaseModel):
    table = 'posts'

    def user(self):
        from .User import User
        return self.belongs_to(User)
