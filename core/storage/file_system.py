import os
from core.config import config

class FileSystem:
    _root = config.APP_URL # Or local path from config
    
    @staticmethod
    def put(path, content, mode='wb'):
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, mode) as f:
            f.write(content)
        return path

    @staticmethod
    def get(path, mode='rb'):
        if os.path.exists(path):
            with open(path, mode) as f:
                return f.read()
        return None

    @staticmethod
    def delete(path):
        if os.path.exists(path):
            os.remove(path)
            return True
        return False

    @staticmethod
    def exists(path):
        return os.path.exists(path)

    @staticmethod
    def size(path):
        return os.path.getsize(path) if os.path.exists(path) else 0
