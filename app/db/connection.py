import psycopg
import os
from dotenv import load_dotenv

load_dotenv()

DB_URL = os.getenv("DATABASE_URL")

def get_connection():
    return psycopg.connect(DB_URL)

def get_user_by_username(username):
    with get_connection() as conn:
        cur = conn.cursor()
        cur.execute("SELECT username, password, role FROM users WHERE username = %s", (username,))
        return cur.fetchone()
