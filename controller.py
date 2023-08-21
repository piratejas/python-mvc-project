import json, requests
from flask import Blueprint, render_template, request
from model import Bid


main = Blueprint("main", __name__)


@main.route("/", methods=["GET", "POST"])
def index():
    headers = {"Content-Type": "application/json", "X-API-Key": "THIS_IS_THE_API_KEY"}
    sort = request.args.get("sort", "")
    offset = int(request.args.get("offset", 0))
    limit = int(request.args.get("limit", 5))
    if request.method == "POST":
        limit = (
            limit if not request.form.get("limit") else int(request.form.get("limit"))
        )
        sort = request.form.get("sort", sort)
    url = f"http://localhost:8080/api/bids?sort={sort}&offset={offset}&limit={limit}"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        bids = response.json()["items"]
        total = response.json()["total_count"]
        return render_template(
            "index.html", bids=bids, total=total, limit=limit, offset=offset, sort=sort
        )
    else:
        message = response.json()["Error"]
        status = response.status_code
        return render_template("error.html", message=message, status=status)


# Controller
@main.route("/add_bid", methods=["POST"])
def add_bid():
    tender = request.form["tender"]
    bid_date = f'{request.form["year"]}-{request.form["month"]}-{request.form["day"]}'
    client = request.form["client"]
    alias = request.form["alias"]
    bid_folder_url = request.form["bid_folder_url"]
    was_successful = request.form["was_successful"]
    data = Bid(
        tender=tender,
        bid_date=bid_date,
        client=client,
        alias=alias,
        bid_folder_url=bid_folder_url,
        was_successful=was_successful,
    )
    url = "http://localhost:8080/api/bids"
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6IlRlc3RlciBNY1Rlc3RmYWNlIiwiYWRtaW4iOmZhbHNlfQ.Dg7f8LVtALYWvjZH31re5C-Pc6Hp6Ra-U4LAy0ZQQ9M",
    }
    response = requests.post(url, headers=headers, data=json.dumps(data.__dict__))
    if response.status_code == 201:
        status = response.status_code
        bid = response.json()
        return render_template("success.html", bid=bid, status=status)
    else:
        message = response.json()["Error"]
        status = response.status_code
        return render_template("error.html", message=message, status=status)
