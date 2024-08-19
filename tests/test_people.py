import allure

from swapi_tests.constants import RESPONSE_BODY_404, RESPONSE_BODY_405
from swapi_tests.model.people import People, ListPeople


@allure.feature('People')
@allure.label('owner', 'Viktoriia Lavrova')
class TestPeople:
    @allure.story('Positive tests')
    class TestPositive:
        def test_get_all_people(self, api_session):
            response = api_session.request(path='people/')
            assert response.status_code == 200
            assert response.headers.get('content-type') == 'application/json'
            ListPeople.model_validate(response.json())

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

        def test_search_people_by_name(self, api_session):
            params = {'search': 'R5-D4'}
            response = api_session.request(path='people/', params=params)
            assert response.status_code == 200
            assert response.headers.get('content-type') == 'application/json'
            person = People.model_validate(response.json()['results'][0])
            # person = ListPeople.model_validate(response.json())
            # assert person.results[0].name == params['search']
            assert person.name == params['search']


    @allure.story('Negative tests')
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

