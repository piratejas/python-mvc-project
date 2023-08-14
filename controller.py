import requests
from flask import Blueprint, render_template, request


main = Blueprint("main", __name__)

# View
@main.route('/')
def index():
    headers = {"Content-Type": "application/json", "X-API-Key": "THIS_IS_THE_API_KEY"}
    response = requests.get("http://localhost:8080/api/bids", headers=headers)
    bids = response.json()["items"]
    return render_template('index.html', bids=bids)

# # Controller
# @app.route('/add_bid', methods=['POST'])
# def add_bid():
#     title = request.form['title']
#     author = request.form['author']
#     book = Book(title, author)
#     # ...
#     # Do something with the book object,
#     # like adding it to a database.
#     # ...
#     return render_template('success.html', book=book)