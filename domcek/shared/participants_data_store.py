from os import path, getcwd
from domcek.shared.abstract_data_store import DataStore


class Participants(DataStore):
    data_path = path.join(getcwd(), 'data/participants.json')
    searchable_fields = ['first_name', 'last_name', 'payment_number', 'birth_date', 'group_name', 'city', 'phone']

    def filter_participants(self, only_participants, search_string=None):
        filtered_list = []

        if search_string == '' or search_string is None or self.data is None:
            return self.data

        filter_strings = search_string.split(' ')

        for subject in self.data:
            matched = False
            if only_participants:
                if subject.get('subscribed', 0):
                    matched = True
            for field in self.searchable_fields:
                if not matched:
                    for text in filter_strings:
                        if text.lower() in str(subject.get(field, '')).lower():
                            matched = True
                        else:
                            matched = False
            if matched:
                filtered_list.append(subject)

        return filtered_list

participants = Participants()
