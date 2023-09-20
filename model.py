import json, os, requests

class Bid:

    def __init__(self, tender, bid_date, client, alias=None, bid_folder_url=None, was_successful=None):
        self.tender = tender
        self.bid_date = bid_date
        self.client = client
        self.alias = alias
        self.bid_folder_url = bid_folder_url
        self.was_successful = was_successful
    
    @classmethod
    def get_all(cls, sort, offset, limit):
        headers = {"Content-Type": "application/json", "X-API-Key": os.getenv("API_KEY")}
        url = f"http://localhost:8080/api/bids?sort={sort}&offset={offset}&limit={limit}"
        response = requests.get(url, headers=headers)
        return response

    @classmethod
    def create_bid(cls, form_data):
        bid_date = f'{form_data["year"]}-{form_data["month"]}-{form_data["day"]}'
        data = cls(
            tender=form_data["tender"],
            bid_date=bid_date,
            client=form_data["client"],
            alias=form_data.get("alias"),
            bid_folder_url=form_data.get("bid_folder_url"),
            was_successful=form_data.get("was_successful")
        )
        return data

    @classmethod
    def add_bid(cls, form_data):
        bid = cls.create_bid(form_data)
        url = "http://localhost:8080/api/bids"
        headers = {
            "Content-Type": "application/json",
            "Authorization": f'Bearer {os.getenv("TOKEN")}',
        }
        response = requests.post(url, headers=headers, data=json.dumps(bid.__dict__))
        return response