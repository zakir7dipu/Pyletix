import secrets

class CSRF:
    @staticmethod
    def generate_token(page):
        token = secrets.token_hex(32)
        page.session.set("_csrf_token", token)
        return token

    @staticmethod
    def validate(page, token):
        stored_token = page.session.get("_csrf_token")
        return stored_token and stored_token == token
