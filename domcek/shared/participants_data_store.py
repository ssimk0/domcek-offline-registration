from os import path, getcwd
from domcek.shared.abstract_data_store import DataStore


class Participants(DataStore):
    data_path = path.join(getcwd() + '/data/participants.json')
    searchable_fields = ['first_name', 'last_name', 'payment_number', 'birth_date', 'group_name', 'city', 'phone']


participants = Participants()
