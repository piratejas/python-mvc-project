from flask import Blueprint, render_template, request
from model import Bid


main = Blueprint("main", __name__)


@main.route("/", methods=["GET", "POST"])
def index():
    sort = request.args.get("sort", "")
    offset = int(request.args.get("offset", 0))
    limit = int(request.args.get("limit", 5))
    if request.method == "POST":
            limit = int(request.form.get("limit", limit))
            sort = request.form.get("sort", sort)

    response = Bid.get_all(sort=sort, offset=offset, limit=limit)
    
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
    


@main.route("/add_bid", methods=["POST"])
def add_bid():
    form_data = request.form.to_dict()
    fields_with_none = ["alias", "bid_folder_url"]
    for field in fields_with_none:
        if field in form_data and form_data[field] == "":
            form_data[field] = None
    form_data["was_successful"] = "was_successful" in form_data
    response = Bid.add_bid(form_data)
    if response.status_code == 201:
        status = response.status_code
        bid = response.json()
        return render_template("success.html", bid=bid, status=status)
    else:
        message = response.json()["Error"]
        status = response.status_code
        return render_template("error.html", message=message, status=status)
