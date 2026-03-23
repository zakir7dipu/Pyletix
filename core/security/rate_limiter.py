import time
from core.database import db

class RateLimiter:
    @staticmethod
    def attempt(key, max_attempts=5, decay_minutes=1):
        # key could be IP or user_id
        now = int(time.time())
        decay_seconds = decay_minutes * 60
        
        # Clean up old records
        db.execute("DELETE FROM rate_limits WHERE expires_at < ?", (now,))
        
        # Check current attempts
        row = db.fetch_one("SELECT attempts FROM rate_limits WHERE key = ?", (key,))
        if row:
            attempts = row['attempts']
            if attempts >= max_attempts:
                return False
            db.execute("UPDATE rate_limits SET attempts = attempts + 1 WHERE key = ?", (key,))
        else:
            db.execute("INSERT INTO rate_limits (key, attempts, expires_at) VALUES (?, ?, ?)", 
                       (key, 1, now + decay_seconds))
        return True

    @staticmethod
    def remaining(key):
        row = db.fetch_one("SELECT attempts FROM rate_limits WHERE key = ?", (key,))
        if row:
            return max(0, 5 - row['attempts']) # Default limit 5
        return 5
