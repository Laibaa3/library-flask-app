import os
from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
from booktxt import Library  # Corrected import

app = Flask(__name__)

# Create a library instance that loads from books.txt
library = Library("books.txt")

@app.route("/", methods=["GET"])
def home():
    current_time = datetime.now()
    return render_template("design.html", books=library.books, current_time=current_time)

@app.route("/reserve", methods=["POST"])
def reserve():
    email = request.form["email"]
    book_id = request.form["book_id"]

    library.reserve_book(book_id, email)
    return redirect(url_for('home'))

@app.route("/cancel", methods=["POST"])
def cancel():
    email = request.form["email"]
    book_id = request.form["book_id"]

    library.cancel_reservation(book_id, email)
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)
