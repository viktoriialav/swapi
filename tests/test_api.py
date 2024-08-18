import pytest

from swapi_tests.api_session import TestSession


@pytest.fixture(scope='session')
def api_session():
    session = TestSession(base_url='https://swapi.dev/api/')
    return session


class TestPeople:
    def test_get_all_people(self, api_session):
        response = api_session.request(path='people/')
        assert response.status_code == 200

    def test_get_first_people(self, api_session):
        response = api_session.request(path='people/1/')
        assert response.status_code == 200
        assert response.json()['name'] == 'Luke Skywalker'

    def test_get_second_people(self, api_session):
        response = api_session.request(path='people/2/')
        assert response.status_code == 200
        assert response.json()['name'] == 'C-3PO'
