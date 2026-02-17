from flask_login import current_user
from app.db.connection import get_connection

def update_stock(product_id, amount):
    with get_connection() as conn:
        cur = conn.cursor()

        # 1️⃣ Lekérjük a jelenlegi készletet
        cur.execute(
            "SELECT quantity FROM products WHERE id=%s FOR UPDATE;",
            (product_id,)
        )
        row = cur.fetchone()

        if not row:
            raise Exception("Product not found")

        quantity_before = row[0]
        quantity_after = quantity_before + amount

        if quantity_after < 0:
            raise Exception("Negative stock not allowed")

        # 2️⃣ Frissítjük a products táblát
        cur.execute(
            "UPDATE products SET quantity=%s WHERE id=%s;",
            (quantity_after, product_id)
        )

        # 3️⃣ Naplózzuk a mozgást
        cur.execute(
            """
            INSERT INTO stock_movements
            (product_id, user_id, change_amount,
             quantity_before, quantity_after, movement_type)
            VALUES (%s, %s, %s, %s, %s, %s);
            """,
            (
                product_id,
                current_user.id,
                amount,
                quantity_before,
                quantity_after,
                "IN" if amount > 0 else "OUT"
            )
        )

        conn.commit()
