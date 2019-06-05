from os import path, getcwd
import locale
from domcek.shared.abstract_data_store import DataStore

locale.setlocale(locale.LC_ALL, "")


def sort_by_last_name(a):
    return locale.strxfrm(a['last_name'])


class Participants(DataStore):
    data_path = path.join(getcwd(), 'data/participants.json')
    searchable_fields = ['first_name', 'last_name', 'payment_number', 'birth_date', 'group_name', 'city', 'phone']

    def filter_participants(self, only_participants, search_string=None):
        filtered_list = []
        filter_strings = []

        self.data.sort(key=sort_by_last_name)

        if (search_string == '' or search_string is None or self.data is None) and only_participants is False:
            return self.data

        if search_string is not None:
            filter_strings = search_string.split(' ')

        for subject in self.data:
            matched = False
            if only_participants and (search_string is None or search_string == ''):
                if subject.get('subscribed', 0):
                    matched = True
            for field in self.searchable_fields:
                if not matched:
                    for text in filter_strings:
                        if text.lower() in str(subject.get(field, '')).lower():
                            if only_participants:
                                if subject.get('subscribed', 0):
                                    matched = True
                            else:
                                matched = True
                        else:
                            matched = False
            if matched:
                filtered_list.append(subject)

        filtered_list.sort(key=sort_by_last_name)
        return filtered_list

    def paid_amount(self):
        paid = 0
        for subject in self.data:
            amount = subject.get('paid', 0) if subject.get('paid', 0) else 0
            paid = paid + amount
        return paid

    def on_reg_amount(self):
        on_reg = 0
        for subject in self.data:
            amount = subject.get('on_registration', 0) if subject.get('on_registration', 0) else 0
            on_reg = on_reg + amount
        return on_reg


participants = Participants()
