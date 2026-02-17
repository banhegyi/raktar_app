# init_db.py
import os
from werkzeug.security import generate_password_hash
import psycopg

# Betöltjük a .env fájlban lévő DB_URL-t
from dotenv import load_dotenv
load_dotenv()

DB_URL = os.getenv("DATABASE_URL")

if not DB_URL:
    raise Exception("DATABASE_URL nincs beállítva a .env fájlban!")

with psycopg.connect(DB_URL) as conn:
    cur = conn.cursor()

    # 1️⃣ Products tábla
    cur.execute("""
    CREATE TABLE IF NOT EXISTS products (
        id SERIAL PRIMARY KEY,
        name VARCHAR(50) NOT NULL,
        sku VARCHAR(30) UNIQUE NOT NULL,
        quantity INTEGER NOT NULL DEFAULT 0,
        location VARCHAR(50)
    );
    """)

    # 2️⃣ Users tábla
    cur.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        username VARCHAR(30) UNIQUE NOT NULL,
        password_hash TEXT NOT NULL,
        role VARCHAR(20) NOT NULL
            CHECK (role IN ('admin', 'raktaros'))
    );
    """)

    # 3️⃣ Stock movements tábla
    cur.execute("""
    CREATE TABLE IF NOT EXISTS stock_movements (
        id SERIAL PRIMARY KEY,
        product_id INTEGER NOT NULL REFERENCES products(id),
        user_id INTEGER NOT NULL REFERENCES users(id),
        change_amount INTEGER NOT NULL,
        quantity_before INTEGER NOT NULL,
        quantity_after INTEGER NOT NULL,
        movement_type VARCHAR(20) NOT NULL
            CHECK (movement_type IN ('IN', 'OUT')),
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """)

    # 4️⃣ Admin user létrehozása (ha még nincs)
    admin_username = "admin"
    admin_password = "admin123"  # ezt később érdemes erősebbre cserélni
    password_hash = generate_password_hash(admin_password)

    cur.execute("SELECT * FROM users WHERE username=%s;", (admin_username,))
    if cur.fetchone() is None:
        cur.execute(
            "INSERT INTO users (username, password_hash, role) VALUES (%s, %s, %s);",
            (admin_username, password_hash, "admin")
        )
        print(f"Admin user létrehozva: {admin_username} / {admin_password}")
    else:
        print("Admin user már létezik")

    conn.commit()
    print("Táblák létrehozva és DB inicializálva ✅")
