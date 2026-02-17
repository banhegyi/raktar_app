from flask import Blueprint, render_template
from app.db.connection import get_connection

products_bp = Blueprint("products", __name__)

@products_bp.route("/")
def index():
    with get_connection() as conn:
        cur = conn.cursor()
        cur.execute("SELECT id, name, sku, quantity FROM products ORDER BY name;")
        products = cur.fetchall()
    return render_template("index.html", products=products)

@products_bp.route("/product/<int:product_id>")
def product(product_id):
    with get_connection() as conn:
        cur = conn.cursor()
        cur.execute("""
            SELECT id, name, sku, quantity, location
            FROM products
            WHERE id = %s
        """, (product_id,))
        product = cur.fetchone()
    return render_template("product.html", product=product)
