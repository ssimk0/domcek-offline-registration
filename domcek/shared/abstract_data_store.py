from os import path
import json


class DataStore:
    data = None
    data_path = None
    searchable_fields = []

    def __init__(self):

        if path.exists(self.data_path):
            with open(self.data_path) as f:
                self.data = json.load(f)

    def store(self, data_to_store=None):
        data_to_store = self.data if data_to_store is None else data_to_store
        with open(self.data_path, 'w+') as outfile:
            json.dump(data_to_store, outfile, indent=4)

        self.data = data_to_store

    def filter(self, search_string=None):
        filtered_list = []

        if search_string == '' or search_string is None or self.data is None:
            return self.data

        filter_strings = search_string.split(' ')

        for subject in self.data:
            matched = False
            for field in self.searchable_fields:
                if not matched:
                    for text in filter_strings:
                        if text.lower() in str(subject.get(field, '')).lower():
                            filtered_list.append(subject)
                            matched = True

        return filtered_list

    def update_by_id(self, subject_id, data):
        for index, subject in enumerate(self.data):
            if subject['id'] == subject_id:
                self.data[index] = data
                break

        self.store()
