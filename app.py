from flask import Flask, render_template, request, redirect, url_for
import database

app = Flask(__name__)

# Home page - show all transactions
@app.route("/")
def index():
    transactions = database.get_all_transactions()
    balance = database.get_balance()
    total_income = database.get_total_income()
    total_expenses = database.get_total_expenses()
    return render_template("index.html", 
                           transactions=transactions,
                           balance=balance,
                           total_income=total_income,
                           total_expenses=total_expenses)

# Add transaction page
@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        type_ = request.form["type"]
        category = request.form["category"]
        amount = float(request.form["amount"])
        note = request.form["note"]
        database.add_transaction(type_, category, amount, note)
        return redirect(url_for("index"))
    return render_template("add.html")

# Delete transaction
@app.route("/delete/<int:id>")
def delete(id):
    database.delete_transaction(id)
    return redirect(url_for("index"))

if __name__ == "__main__":
    database.init_db()
    app.run(debug=True)