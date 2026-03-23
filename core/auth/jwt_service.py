import jwt
import datetime
from core.config import config

class JWTService:
    _secret = config.APP_KEY or "secret_key_change_me"

    @classmethod
    def generate(cls, user_id):
        payload = {
            "user_id": user_id,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(days=7),
            "iat": datetime.datetime.utcnow()
        }
        return jwt.encode(payload, cls._secret, algorithm="HS256")

    @classmethod
    def validate(cls, token):
        try:
            payload = jwt.decode(token, cls._secret, algorithms=["HS256"])
            return payload
        except jwt.ExpiredSignatureError:
            return None
        except jwt.InvalidTokenError:
            return None
