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
    


# @main.route("/add_bid", methods=["POST"])
# def add_bid():
#     data = Bid(
#         tender=request.form["tender"],
#         bid_date=f'{request.form["year"]}-{request.form["month"]}-{request.form["day"]}',
#         client=request.form["client"],
#         alias=request.form["alias"],
#         bid_folder_url=request.form["bid_folder_url"],
#         was_successful=request.form["was_successful"],
#         feedback = {"description": request.form["feedback_description"], "url": request.form["feedback_url"]}
#     )
#     url = "http://localhost:8080/api/bids"
#     headers = {
#         "Content-Type": "application/json",
#         "Authorization": f'Bearer {os.getenv("TOKEN")}',
#     }
#     response = requests.post(url, headers=headers, data=json.dumps(data.__dict__))
#     if response.status_code == 201:
#         status = response.status_code
#         bid = response.json()
#         return render_template("success.html", bid=bid, status=status)
#     else:
#         message = response.json()["Error"]
#         status = response.status_code
#         return render_template("error.html", message=message, status=status)
