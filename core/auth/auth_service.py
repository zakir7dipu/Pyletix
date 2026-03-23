import bcrypt
import secrets

class Hash:
    @staticmethod
    def make(password):
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
        return hashed.decode('utf-8')

    @staticmethod
    def check(password, hashed_password):
        return bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))

class Auth:
    _user = None

    @classmethod
    def login(cls, user, page, remember=False):
        cls._user = user
        page.session.set("user_id", user.id)
        if remember:
            # Token logic for remember me
            token = secrets.token_hex(32)
            # Store token in DB linked to user
            pass

    @classmethod
    def user(cls, page):
        if cls._user:
            return cls._user
        
        user_id = page.session.get("user_id")
        if user_id:
            from app.models.User import User
            cls._user = User.find(user_id)
            return cls._user
        return None

    @classmethod
    def logout(cls, page):
        cls._user = None
        page.session.remove("user_id")

    @classmethod
    def check(cls, page):
        return cls.user(page) is not None
