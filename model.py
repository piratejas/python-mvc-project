import os, requests
from flask import request

class Bid:

    def __init__(self, tender, bid_date, client, alias=None, bid_folder_url=None, was_successful=None, feedback=None):
        self.tender = tender
        self.bid_date = bid_date
        self.client = client
        self.alias = alias
        self.bid_folder_url = bid_folder_url
        self.was_successful = was_successful
        self.feedback = feedback
    
    @classmethod
    def get_all(cls, sort, offset, limit):
        headers = {"Content-Type": "application/json", "X-API-Key": os.getenv("API_KEY")}
        if request.method == "POST":
            limit = int(request.form.get("limit", limit))
            sort = request.form.get("sort", sort)
        url = f"http://localhost:8080/api/bids?sort={sort}&offset={offset}&limit={limit}"
        response = requests.get(url, headers=headers)

        return response
