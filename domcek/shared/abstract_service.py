import requests
from domcek.shared.participants_data_store import participants
from domcek.shared.wrong_payments_data_store import wrong_payments


class Service:
    api_root = 'https://api.domcek.org/api'
    participant_store = None
    wrong_payments_store = None

    def __init__(self):
        self.participant_store = participants
        self.wrong_payments_store = wrong_payments

    def make_request(self, method, uri, data=None, params=None):
        data = data if data else {}
        return requests.request(method, self.api_root + uri, json=data, params=params)
