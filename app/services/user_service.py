from flask_login import UserMixin
from app.db.connection import get_connection

class User(UserMixin):
    def __init__(self, id, username, role):
        self.id = id
        self.username = username
        self.role = role

def get_user_by_username(username):
    with get_connection() as conn:
        cur = conn.cursor()
        cur.execute(
            "SELECT id, username, password_hash, role FROM users WHERE username=%s",
            (username,)
        )
        return cur.fetchone()

def get_user_by_id(user_id):
    with get_connection() as conn:
        cur = conn.cursor()
        cur.execute(
            "SELECT id, username, role FROM users WHERE id=%s",
            (user_id,)
        )
        row = cur.fetchone()
        if row:
            return User(*row)
