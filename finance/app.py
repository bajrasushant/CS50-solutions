import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime
from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

db.execute("CREATE TABLE IF NOT EXISTS orders (id INTEGER, user_id NUMERIC NOT NULL, symbol TEXT NOT NULL, \
            shares NUMERIC NOT NULL, price NUMERIC NOT NULL, time TEXT NOT NULL, PRIMARY KEY(id), \
            FOREIGN KEY(user_id) REFERENCES users(id))")

db.execute("CREATE INDEX IF NOT EXISTS idx_order_user_id ON orders(user_id)")

# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""

    user_id = session["user_id"]
    stocks_owned = db.execute("SELECT * FROM orders WHERE user_id = ?", user_id)

    share_owned = dict()
    # create a final dictionary of stocks its number of shares
    for i in stocks_owned:
        symbol, shares = i["symbol"], i["shares"]
        share_owned[symbol] = share_owned.setdefault(symbol, 0) + shares

    # amount total
    total = 0

    for symbol, shares in share_owned.items():
        # getting recent price
        # lookup returns dict in order of name->price->symbol
        result = lookup(symbol)
        name, price = result["name"], result["price"]
        stock_current_value = shares * price
        total+=stock_current_value
        # creating a key-value pair of symbol and tuple
        share_owned[symbol] = (name, shares, usd(price), usd(stock_current_value))
    cash = db.execute("SELECT cash FROM users WHERE id = ?", user_id)[0]["cash"]
    total+=cash
    return render_template("index.html", share_owned=share_owned, cash=usd(cash), total=usd(total))

@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    if request.method == "GET":
        return render_template("buy.html")
    else:
        stockSymbol = request.form.get("symbol")
        stockData = lookup(stockSymbol)
        shares = request.form.get("shares")
        if not stockSymbol or stockData==None:
            return apology("Enter a valid stock symbol!")
        if int(shares) < 0:
            return apology("Number of shares should not be less than zero")

        stock_name = stockData["name"]
        stock_price = stockData["price"]
        stock_symbol = stockData["symbol"]
        user_id = session["user_id"]
        # cash in hand
        cash = db.execute("SELECT cash FROM users WHERE id = ?", user_id)[0]["cash"]
        current_time = datetime.now().strftime("%H:%M:%S")
        # can buy?
        remaining_amount = cash - float(shares) * stock_price;
        if remaining_amount < 0:
            return apology("Insufficient funds")

        # update cash in hand of the user
        db.execute("UPDATE users SET cash = ? WHERE id = ?", remaining_amount, user_id)

        # update the orders given by the user
        # db.execute("CREATE TABLE IF NOT EXISTS orders (id INTEGER, user_id NUMERIC NOT NULL, symbol TEXT NOT NULL, \
        #     shares NUMERIC NOT NULL, price NUMERIC NOT NULL, time TEXT NOT NULL, PRIMARY KEY(id), \
        #     FOREIGN KEY(user_id) REFERENCES users(id))")

        db.execute("INSERT INTO orders (user_id, symbol, shares, price, time) VALUES (?, ?, ?, ?, ?)", \
                    user_id, stock_symbol, shares, stock_price, current_time)

        return redirect("/")

@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    user_id = session["user_id"]

    transactions = db.execute("SELECT * FROM orders WHERE user_id=?", user_id)
    return render_template("history.html", transactions=transactions)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    if request.method == "GET":
        return render_template("quote.html")
    else:
        stock_symbol = request.form.get("symbol")
        stock_data = lookup(stock_symbol)

        if not stock_data:
            return render_template("quote.html", invalid=True, symbol=stock_symbol)
        return render_template("quoted.html", name=stock_data["name"], symbol=stock_data["symbol"], price=stock_data["price"])


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    session.clear()
    # access using get
    if request.method == "GET":
        return render_template("register.html")
    else:
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")
        # requires a username password and confirmation
        if (not username or not password or not confirmation):
            return apology("all three fields required")
        # checking password and confirmation
        if password != confirmation:
            return apology("passwords do not match")

        #checking if username exists
        rows = db.execute("SELECT * FROM users WHERE username = ?", username)
        if (len(rows) > 1):
            return apology("Try again username already exists")

        db.execute('INSERT INTO users (username, hash) VALUES(?, ?)', username, generate_password_hash(password))

        flash("You have been registered")

        return render_template("login.html")

@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    user_id = session["user_id"]
    stocks_owned = db.execute("SELECT * FROM orders WHERE user_id = ?", user_id)
    share_owned = dict()
    # create a final dictionary of stocks its number of shares
    for i in stocks_owned:
        symbol, shares = i["symbol"], i["shares"]
        share_owned[symbol] = share_owned.setdefault(symbol, 0) + shares

    if request.method == "GET":
        return render_template("sell.html", share_owned=share_owned)
    else:
        stock_to_sell = request.form.get("symbol")
        num_shares_to_sell = request.form.get("shares")
        if not stock_to_sell or not num_shares_to_sell:
            return apology("Choose a stock to sell")
        if int(num_shares_to_sell) > int(share_owned[stock_to_sell]):
            return apology("Not sufficient shares")

        stock_data = lookup(stock_to_sell)
        stock_price = stock_data["price"]
        stock_symbol = stock_data["symbol"]
        stock_sales = int(num_shares_to_sell) * stock_price
        num_shares_to_sell = 0 - int(num_shares_to_sell)
        current_time = datetime.now().strftime("%H:%M:%S")

        db.execute("INSERT INTO orders(user_id, symbol, shares, price, time) VALUES(?, ?, ?, ?, ?)", user_id, stock_symbol, num_shares_to_sell, stock_price, current_time)

        cash = db.execute("SELECT cash FROM users WHERE id = ?", user_id)[0]["cash"]
        remaining_amount = cash + stock_sales
        db.execute("UPDATE users SET cash = ? WHERE id = ?", remaining_amount, user_id)
        return redirect('/')

        # result = int(share_owned[stock_to_sell]) - int(num_shares_to_sell)

        # current_time = datetime.now().strftime("%H:%M:%S")
        # stock_current = lookup(stock_to_sell)
        # stock_symbol = stock_current["symbol"]
        # stock_price = stock_current["price"]

        # stock_sales = int(num_shares_to_sell) * stock_price

        # cash = db.execute("SELECT cash FROM users WHERE id = ?", user_id)[0]["cash"]
        # remaining_amount = cash + stock_sales
        # db.execute("UPDATE users SET cash = ? WHERE id = ?", remaining_amount, user_id)

        # db.execute("DELETE FROM orders WHERE symbol=?", stock_to_sell)
        # db.execute("INSERT INTO orders(user_id, symbol, shares, price, time) VALUES(?, ?, ?, ?, ?)", user_id, stock_symbol, result, stock_price, current_time)


