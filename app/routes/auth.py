from flask import Blueprint, render_template, request, redirect
from flask_login import login_user, logout_user
from werkzeug.security import check_password_hash
from app.services.user_service import get_user_by_username, User

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user_row = get_user_by_username(request.form["username"])

        if user_row and check_password_hash(
            user_row[2], request.form["password"]
        ):
            user = User(user_row[0], user_row[1], user_row[3])
            login_user(user)
            return redirect("/")

        return "Login failed"

    return render_template("login.html")

@auth_bp.route("/logout")
def logout():
    logout_user()
    return redirect("/login")
