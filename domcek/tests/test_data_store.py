import pytest
import json
from os import path, remove
from domcek.shared.abstract_data_store import DataStore


@pytest.fixture
def test_data_store():
    data = [
        {
            'id': 1,
            'name': 'John',
            'email': 'john@example.com'
        },
        {
            'id': 2,
            'name': 'Jane',
            'email': 'jane@example.com',
            'registered': True,
            'city': 'Kosice'
        }
    ]
    with open(path.join(path.join(path.dirname(__file__)), '../test_data/sample_data.json'), 'w+') as outfile:
        json.dump(data, outfile, indent=4)

    class testData(DataStore):
        data_path = path.join(path.join(path.dirname(__file__)), '../test_data/sample_data.json')
        searchable_fields = ['name', 'email', 'city']

    return testData()


@pytest.fixture
def empty_data_store():
    data_path = path.join(path.join(path.dirname(__file__)), '../test_data/wrong_path_data.json')

    ## cleanup before test
    if path.exists(data_path):
        remove(data_path)

    class testData(DataStore):
        data_path = path.join(path.join(path.dirname(__file__)), '../test_data/wrong_path_data.json')
        searchable_fields = ['name', 'email', 'city']

    return testData()


# Data should load in class constructor, and should exist if file are there
def test_loading_data(test_data_store):
    assert len(test_data_store.data) == 2


# Data should load in class constructor, and should be None if file not exist
def test_loading_data_from_not_existing_file(empty_data_store):
    assert empty_data_store.data is None


def test_store_should_create_file(empty_data_store):
    empty_data_store.store({
        'test': 'test'
    })

    assert path.exists(empty_data_store.data_path) == True


def test_store_should_store_data_in_class(empty_data_store):
    empty_data_store.store({
        'test': 'test'
    })

    assert empty_data_store.data['test'] == 'test'


def test_store_should_overide_your_data(test_data_store):
    assert test_data_store.data[0]['name'] == 'John'

    test_data_store.store({
        'test': 'test'
    })

    assert test_data_store.data['test'] == 'test'


def test_filter_data(test_data_store):
    data = test_data_store.filter('John')

    assert len(data) == 1
    assert data[0]['name'] == 'John'
    assert data[0]['id'] == 1


# Filter should return empty list if data not match filer
def test_filter_should_return_empty_list(test_data_store):
    data = test_data_store.filter('Smith')

    assert len(data) == 0


# Filter should return None if there are no data
def test_filter_should_return_none(empty_data_store):
    data = empty_data_store.filter('John Smith')

    assert data is None


def test_update_by_id(test_data_store):
    test_data_store.update_by_id(1, {
        'id': 1,
        'name': 'John Smith',
        'email': 'john@example.com'
    })

    assert test_data_store.data[0]['name'] is 'John Smith'


def test_find_by(test_data_store):
    data = test_data_store.find_by('jane@example.com', 'email')

    assert data['name'] == 'Jane'
