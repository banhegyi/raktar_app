import os
import psycopg
from flask import Flask, render_template
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

DB_URL = os.getenv("DATABASE_URL")

def get_connection():
    return psycopg.connect(DB_URL)

@app.route("/")
def index():
    with get_connection() as conn:
        cur = conn.cursor()
        cur.execute("SELECT id, name, sku, quantity FROM products ORDER BY name;")
        products = cur.fetchall()
    return render_template("index.html", products=products)

@app.route("/product/<int:product_id>")
def product(product_id):
    with get_connection() as conn:
        cur = conn.cursor()
        cur.execute("SELECT id, name, sku, quantity, location FROM products WHERE id = %s;", (product_id,))
        product = cur.fetchone()
    return render_template("product.html", product=product)
