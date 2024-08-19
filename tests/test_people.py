from swapi_tests.constants import RESPONSE_BODY_404, RESPONSE_BODY_405
from swapi_tests.model.people import People, ListPeople


class TestPeople:
    class TestPositive:
        def test_get_all_people(self, api_session):
            response = api_session.request(path='people/')
            assert response.status_code == 200
            assert response.headers.get('content-type') == 'application/json'
            people = ListPeople.model_validate(response.json())

        def test_get_first_people(self, api_session):
            response = api_session.request(path='people/1/')
            assert response.status_code == 200
            assert response.headers.get('content-type') == 'application/json'
            person = People.model_validate(response.json())
            assert person.name == 'Luke Skywalker'

        def test_get_second_people(self, api_session):
            response = api_session.request(path='people/2/')
            assert response.status_code == 200
            assert response.headers.get('content-type') == 'application/json'
            person = People.model_validate(response.json())
            assert person.name == 'C-3PO'

        def test_get_without_header_user_agent(self, api_destruction_session):
            api_destruction_session.headers.pop('user-agent')
            response = api_destruction_session.request(path='people/')
            assert response.status_code == 200
            assert response.headers.get('content-type') == 'application/json'

    class TestNegative:
        def test_get_404(self, api_session):
            response = api_session.request(path='wrong/')
            assert response.status_code == 404
            assert response.headers.get('content-type') == 'text/html'

        def test_get_405(self, api_session):
            response = api_session.request(path='people/', method='POST')
            assert response.status_code == 405
            assert response.json() == RESPONSE_BODY_405

        def test_wrong_query(self, api_session):
            response = api_session.request(path='people/adsdasd')
            assert response.status_code == 404
            assert response.json() == RESPONSE_BODY_404

