import sqlite3
import os
from ..config import config

class Database:
    _connection = None

    @classmethod
    def get_connection(cls):
        if cls._connection is None:
            db_path = config.DB_DATABASE
            db_dir = os.path.dirname(db_path)
            if not os.path.exists(db_dir):
                os.makedirs(db_dir, exist_ok=True)
            
            cls._connection = sqlite3.connect(db_path, check_same_thread=False)
            cls._connection.row_factory = sqlite3.Row
        return cls._connection

    @classmethod
    def execute(cls, query, params=None):
        conn = cls.get_connection()
        cursor = conn.cursor()
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)
        conn.commit()
        return cursor

    @classmethod
    def fetch_all(cls, query, params=None):
        cursor = cls.execute(query, params)
        return cursor.fetchall()

    @classmethod
    def fetch_one(cls, query, params=None):
        cursor = cls.execute(query, params)
        return cursor.fetchone()

db = Database
