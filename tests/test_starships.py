import allure

from swapi_tests.models.starships import ListStarShips, StarShip
from swapi_tests.utils.constants import RESPONSE_BODY_404, RESPONSE_BODY_405


@allure.feature('StarShips')
@allure.label('owner', 'Viktoriia Lavrova')
class TestStarShips:
    @allure.story('Positive tests')
    class TestPositive:
        def test_get_all_starships(self, api_session):
            response = api_session.request(path='starships/')
            assert response.status_code == 200
            assert response.headers.get('content-type') == 'application/json'
            ListStarShips.model_validate(response.json())

        def test_get_second_starship(self, api_session):
            response = api_session.request(path='starships/2/')
            assert response.status_code == 200
            assert response.headers.get('content-type') == 'application/json'
            starship = StarShip.model_validate(response.json())
            assert starship.name == 'CR90 corvette'

        def test_get_nine_starship(self, api_session):
            response = api_session.request(path='starships/9/')
            assert response.status_code == 200
            assert response.headers.get('content-type') == 'application/json'
            starship = StarShip.model_validate(response.json())
            assert starship.name == 'Death Star'

        def test_search_particular_starship_by_name(self, api_session):
            params = {'search': 'X-wing'}
            response = api_session.request(path='starships/', params=params)
            assert response.status_code == 200
            assert response.headers.get('content-type') == 'application/json'
            starship = ListStarShips.model_validate(response.json())
            assert starship.results[0].name == params['search']

        def test_search_starship_by_model(self, api_session):
            params = {'search': 'YT-1300 light freighter'}
            response = api_session.request(path='starships/', params=params)
            assert response.status_code == 200
            assert response.headers.get('content-type') == 'application/json'
            starship = ListStarShips.model_validate(response.json())
            assert starship.results[0].model == params['search']

        def test_search_starships_by_part_of_name_or_model(self, api_session):
            params = {'search': 'r'}
            response = api_session.request(path='starships/', params=params)
            assert response.status_code == 200
            assert response.headers.get('content-type') == 'application/json'
            starships = ListStarShips.model_validate(response.json())
            assert sum(
                params['search'].lower() in starship.name.lower() or params['search'].lower() in starship.model.lower()
                for starship in starships.results) == len(starships.results)
            pass

    @allure.story('Negative tests')
    class TestNegative:
        def test_get_405(self, api_session):
            response = api_session.request(path='starships/', method='POST')
            assert response.status_code == 405
            assert response.json() == RESPONSE_BODY_405

        def test_wrong_query(self, api_session):
            response = api_session.request(path='starships/adsdasd')
            assert response.status_code == 404
            assert response.json() == RESPONSE_BODY_404
