from flask import Blueprint, render_template
from app.db.connection import get_connection

stock_bp = Blueprint("stock", __name__, url_prefix="/stock")

@stock_bp.route("/")
def stock_movements():
    with get_connection() as conn:
        cur = conn.cursor()
        cur.execute("""
            SELECT id, product_id, user, quantity_change, timestamp
            FROM stock_movements
            ORDER BY timestamp DESC;
        """)
        movements = cur.fetchall()
    return render_template("stock_movements.html", movements=movements)
