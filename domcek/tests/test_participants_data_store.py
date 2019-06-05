import pytest
import json
from os import path, getcwd, remove
from domcek.shared.participants_data_store import Participants


@pytest.fixture
def test_data_store():
    data = [
        {
            'id': 1,
            'name': 'John',
            'last_name': 'X',
            'email': 'john@example.com',
            'subscribed': 1,
            'paid': 10,
            'on_registration': 0
        },
        {
            'id': 2,
            'name': 'Jane',
            'last_name': 'Y',
            'email': 'jane@example.com',
            'registered': True,
            'city': 'Kosice'
        }
    ]
    with open(path.join(getcwd(), 'test_data/participant.json'), 'w+') as outfile:
        json.dump(data, outfile, indent=4)

    class testData(Participants):
        data_path = path.join(getcwd(), 'test_data/participant.json')
        searchable_fields = ['name', 'email', 'city']

    return testData()


def test_filter_only_participants(test_data_store):
    assert len(test_data_store.data) == 2

    data = test_data_store.filter_participants(True, 'Jane')

    assert len(data) == 0


def test_filter_only_participants_founded(test_data_store):
    assert len(test_data_store.data) == 2

    data = test_data_store.filter_participants(True, 'John')

    assert len(data) == 1
