import requests
import os
from domcek.shared.participants_data_store import participants
from domcek.shared.wrong_payments_data_store import wrong_payments


class Service:
    api_root = 'https://api.domcek.org/api'
    participant_store = None
    wrong_payments_store = None

    def __init__(self):
        self.participant_store = participants
        self.wrong_payments_store = wrong_payments

    def make_request(self, method, uri, data=None):
        data = data if data else {}
        params = {
            'token': os.environ['API_TOKEN']
        }
        return requests.request(method, self.api_root + uri, data=data, params=params)
