# app/models.py
from flask_login import UserMixin
from app.db.connection import get_user_by_username

class User(UserMixin):
    def __init__(self, username, password, role):
        self.id = username
        self.password = password
        self.role = role

    @staticmethod
    def get_by_id(username):
        data = get_user_by_username(username)
        if data:
            return User(*data)
        return None
