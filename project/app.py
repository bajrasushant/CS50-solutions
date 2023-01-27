import os


from flask import Flask, flash, redirect, render_template, request, session
from flask_session  import Session
from cs50 import SQL
from werkzeug.security import check_password_hash, generate_password_hash
from helpers import apology, login_required, password_check

app = Flask(__name__)

app.config["SESSSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

db = SQL("sqlite:///final.db")

# db = conn.cursor()
db.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, username TEXT NOT NULL, hash TEXT NOT NULL)")
db.execute("CREATE UNIQUE INDEX IF NOT EXISTS username ON users(username)")
# conn.commit()

@app.route("/")
@login_required
def index():
    return apology("todo")

@app.route("/todo", methods=["GET", "POST"])
@login_required
def todo():
    return apology("todo")

@app.route("/note", methods=["GET", "POST"])
@login_required
def note():
    return apology("todo")

@app.route("/login", methods=["GET", "POST"])
def login():
    session.clear()

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        if not username:
            return apology("Must provide a username")

        elif not password:
            return apology("Most provide your password")

        rows = db.execute("SELECT * FROM users WHERE username = ?", username)

        if (len(rows) != 1 or not check_password_hash(rows[0]["hash"], password)):
            return apology("Invalid username and/or password")

        session["user_id"] = rows[0]["id"]

        return redirect("/")

    else:
        return render_template("login.html")

@app.route("/logout")
def logout():
    # remove the user
    session.clear()

    # redirect to login
    return redirect("/")

@app.route("/register", methods=["GET", "POST"])
def register():
    session.clear()
    if request.method == "GET":
        return render_template("register.html")
    else:
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        if (not username or not password or not confirmation):
            return apology("Must require all 3 to be filled")

        # if not password_check(password):
        #     return apology("Your password must require at least a digit & a unique symbol & atleast 8 characters")

        if password != confirmation:
            return apology("Passwords do not match")

        rows = db.execute("SELECT * FROM users WHERE username = ?", username)

        if (len(rows) > 0):
            return apology("Username already taken")

        password_hash = generate_password_hash(password)
        db.execute("INSERT INTO users(username, hash) VALUES(?, ?)", username, password_hash)

        rows = db.execute("SELECT * FROM users WHERE username = ?", username)

        session["user_id"] = rows[0]["id"]
        return redirect("/")



