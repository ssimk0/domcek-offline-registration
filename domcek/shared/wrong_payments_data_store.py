from os import path, getcwd
from domcek.shared.abstract_data_store import DataStore


class WrongPayments(DataStore):
    data_path = path.join(getcwd() + '/data/wrong_payments.json')
    searchable_fields = ['payment_note', 'amount', 'payment_number', 'iban', 'transaction_date']


wrong_payments = WrongPayments()
