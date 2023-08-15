import requests
from flask import Blueprint, render_template, request


main = Blueprint("main", __name__)


@main.route('/', methods=["GET", "POST"])
def index():
    headers = {"Content-Type": "application/json", "X-API-Key": "THIS_IS_THE_API_KEY"}
    offset = int(request.args.get("offset", 0))
    limit = int(request.args.get("limit", 0))
    if request.method == "POST":
        limit = int(request.form["limit"])
    last_offset = offset - limit
    next_offset = offset + limit
    url = f"http://localhost:8080/api/bids?offset={offset}&limit={limit}"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        bids = response.json()["items"]
        return render_template('index.html', bids=bids, limit=limit, offset=offset, next_offset=next_offset, last_offset=last_offset)
    else:
        return render_template('error.html', error=response.json(), status=response.status_code)
        

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