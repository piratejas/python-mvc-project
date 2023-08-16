import requests
from flask import Blueprint, render_template, request


main = Blueprint("main", __name__)


@main.route('/', methods=["GET", "POST"])
def index():
    headers = {"Content-Type": "application/json", "X-API-Key": "THIS_IS_THE_API_KEY"}
    sort = request.args.get("sort", "")
    offset = int(request.args.get("offset", 0))
    limit = int(request.args.get("limit", 5))
    if request.method == "POST":
        limit = limit if not request.form.get("limit") else int(request.form.get("limit"))
        sort = request.form.get("sort", sort)
    url = f"http://localhost:8080/api/bids?sort={sort}&offset={offset}&limit={limit}"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        bids = response.json()["items"]
        return render_template('index.html', bids=bids, limit=limit, offset=offset, sort=sort)
    else:
        message = response.json()["Error"]
        status=response.status_code
        return render_template('error.html', message=message, status=status)
        

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