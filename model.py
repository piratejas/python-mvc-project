import requests

# # Model
# class Book:
#     # Instead of a simple class,
#     # a database model would more likely to be used.
#     def __init__(self, title, author):
#         self.title = title
#         self.author = author

class Bid:
    def __init__(self,tender, bid_date, client, alias=None, bid_folder_url=None, was_successful=None, feedback=None):
        self.tender = tender
        self.bid_date = bid_date
        self.client = client
        self.alias = alias
        self.bid_folder_url = bid_folder_url
        self.was_successful = was_successful
        self.feedback = feedback
    def get_all(self):
        pass