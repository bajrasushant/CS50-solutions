import os
import sqlite3

from flask import Flask, flash, redirect, render_template, request, session
from flask_session  import Session
from cs50 import SQL
from helpers import apology, login_required, password_check

app = Flask(__name__)

app.config["SESSSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

try:
    db = SQL("sqlite:///final.db")
except:
    db = sqlite3.connect('final')
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

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

@app.route("/register", methods=["GET", "POST"])
def register():
    return apology("todo")

