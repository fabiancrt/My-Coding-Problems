import os



#ANSWERS WRITTEN BY FABIAN C.




from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

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


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

#INDEX
@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""

    # QUERY FOR USER
    user_portfolio = db.execute(
        "SELECT id, symbol, name, SUM(shares)  FROM trans WHERE id = ? GROUP BY symbol HAVING SUM(shares) > 0 ORDER BY price DESC", session["user_id"])

    user_cash = db.execute("SELECT * FROM users WHERE id = ?", session["user_id"])

    # UPDATE PORTFOLIO
    current_worth = 0
    for stock in user_portfolio:
        stock_data = lookup(stock["symbol"])
        stock["currentprice"] = stock_data["price"]
        stock["totalprice"] = stock_data["price"] * stock["SUM(shares)"]
        current_worth += stock["totalprice"]

    return render_template("index.html", user_portfolio=user_portfolio, user_cash=user_cash, current_worth=current_worth)

#BUY METHOD
@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    # POST ROUTE!
    if request.method == "POST":
        symbol = request.form.get("symbol")
        shares_nbr = request.form.get("shares")

        # SYMBOL VERIFICATIONS
        if symbol == "":
            return apology("MISSING SYMBOL", 400)
        if shares_nbr == "" or shares_nbr.isalpha():
            return apology("MISSING SHARES", 400)
        if not shares_nbr.isdigit():
            return apology("INAPPROPRIATE SHARE", 400)
        if int(shares_nbr) <= 0:
            return apology("SHARE >= 0", 400)

        stock_quote = lookup(symbol.upper())

        if not stock_quote:
            return apology("INVALID SYMBOL", 400)

        total_cost = int(shares_nbr) * stock_quote["price"]

        user_cash = db.execute("SELECT * FROM users WHERE id = ?", session["user_id"])

        if user_cash[0]["cash"] < total_cost:
            return apology("CAN'T AFFORD", 400)

        else:
            db.execute("INSERT INTO trans (id, symbol, shares, price) VALUES(?, ?, ?, ?)",
                       session["user_id"],stock_quote['symbol'], int(shares_nbr),stock_quote['price'])
            cash = user_cash[0]["cash"]
            db.execute("UPDATE users SET cash = ? WHERE id = ?", cash - total_cost, session["user_id"])
            flash('Bought!')
            return redirect("/")

    # GET ROUTE!
    else:
        return render_template("buy.html")

#HISTORY
@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    # QUERY FOR USER & TRANSACTIONS
    user_transactions = db.execute(
        "SELECT id, symbol, shares, price, transacted  FROM trans WHERE id = ? ORDER BY transacted", session["user_id"])

    return render_template("history.html", user_transactions=user_transactions)

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
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(
            rows[0]["hash"], request.form.get("password")
        ):
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

#QUOTE
@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""

    # POST ROUTE!
    if request.method == "POST":
        symbol = request.form.get("symbol")
        # SYMBOL != NULL
        if symbol == "":
            return apology("PLEASE INPUT VALUE", 400)

        stock_quote = lookup(symbol)

        if not stock_quote:
            return apology("INVALID SYMBOL", 400)
        else:
            return render_template("quoted.html", symbol=stock_quote)

    # GET ROUTE !
    else:
        return render_template("quote.html")


#REGISTRATION
@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""

    # CLEAR SESSION ID
    session.clear()

    # POST ROUTE
    if request.method == "POST":

        # VALIDATION
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        # QUERY
        rows = db.execute("SELECT * FROM users WHERE username = ?", username)

        # VERIFY PASSWORD
        if not (password == confirmation):
            return apology("Passwords don't match", 400)

        # PASSWORD != NULL
        if password == "" or confirmation == "" or username == "":
            return apology("Please Input Value", 400)

        # UNIQUE USERNAME
        if len(rows) == 1:
            return apology("Username in use", 400)
        else:
            hash = generate_password_hash(password)
            db.execute("INSERT INTO users (username, hash) VALUES(?, ?)", username, hash)

        # REDIRECT INDEX
        return redirect("/")

    else:
        return render_template("register.html")

#SELL FUNCTION
@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    #POST ROUTE
    if request.method == "POST":
        symbol = request.form.get("symbol")
        shares_nbr = request.form.get("shares")

        # SYMBOL != NULL
        if symbol == "":
            return apology("MISSING SYMBOL", 400)
        if shares_nbr == "" or shares_nbr.isalpha():
            return apology("MISSING SHARES", 400)
        # SYMBOL IS APPROPRIATE
        if not shares_nbr.isdigit():
            return apology("INAPPROPRIATE SYMBOL", 400)
        # SYMBOL IS GREATER THAN 0
        if int(shares_nbr) <= 0:
            return apology("SYMBOL > = 0", 400)
        stock_quote = lookup(symbol)

        if not stock_quote:
            return apology("INAPPROPRIATE SYMBOL", 400)

        user_portfolio = db.execute("SELECT id, symbol, SUM(shares) FROM trans WHERE id = ? AND symbol = ? GROUP BY symbol HAVING SUM(shares)>0 ", session["user_id"], stock_quote['symbol'])
        user_cash = db.execute("SELECT * FROM users WHERE id = ?", session["user_id"])

        user_cash = db.execute("SELECT * FROM users WHERE id = ?", session["user_id"])

        if user_portfolio[0]["SUM(shares)"] < int(shares_nbr):
            return apology("TOO MANY SHARES", 400)
        else:
            #UPDATE USER PORTFOLIO

            currentprice = stock_quote['price'] * int(shares_nbr)
            cash = user_cash[0]["cash"]
            db.execute("UPDATE users SET cash = ? WHERE id = ?", cash + currentprice, session["user_id"])
            db.execute("INSERT INTO trans (id, symbol, shares, price) VALUES(?, ?, ?, ?)",
                       session["user_id"], stock_quote['symbol'], -int(shares_nbr), stock_quote['price'])
            flash('Sold!')
        return redirect("/")

    # GET ROUTE!
    else:
        user_portfolio = db.execute(
            "SELECT id, symbol, SUM(shares) FROM trans WHERE id = ? GROUP BY symbol HAVING SUM(shares)>0 ORDER BY symbol", session["user_id"])

        return render_template("sell.html", user_portfolio=user_portfolio)

#PERSONAL TOUCH -- ADDING CASH TO YOUR BALANCE
@app.route("/add_cash", methods=["GET", "POST"])
@login_required
def add_cash():
    """ADD CASH TO YOUR BALANCE"""
    if request.method == "GET":
        return render_template("add_cash.html")
    else:
        new_cash = int(request.form.get("new_cash"))

        if not new_cash:
            return apology("PLEASE INPUT CASH")

        user_id = session["user_id"]
        user_cash_db = db.execute("SELECT cash FROM users WHERE id = ?", user_id)
        user_cash = user_cash_db[0]["cash"]

        uptd_cash = user_cash + new_cash

        db.execute("UPDATE users SET cash = ? WHERE id = ?", uptd_cash, user_id)

        return redirect("/")
