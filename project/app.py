import os
import sqlite3

from flask import Flask, flash, redirect, render_template, requeset, session
from flask_session  import Session
from cs50 import SQL
from helpers import apology, login_required

app = Flask(__name__)

app.config["SESSSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

try:
    db = SQL("sqlite:///final.db")
except:
    db = sqlite3.connect('final')
    db = conn.cursor()
    db.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, username TEXT NOT NULL, hash TEXT NOT NULL)")
    db.execute("CREATE UNIQUE INDEC IF NOT EXISTS username ON users(username)")
    conn.commit()




