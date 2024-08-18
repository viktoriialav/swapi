from swapi_tests.constants import RESPONSE_BODY_404, RESPONSE_BODY_405


class TestStarShips:
    class TestPositive:
        def test_get_all_starships(self, api_session):
            response = api_session.request(path='starships/')
            assert response.status_code == 200
            assert response.headers.get('content-type') == 'application/json'

        def test_get_second_starship(self, api_session):
            response = api_session.request(path='starships/2/')
            assert response.status_code == 200
            assert response.headers.get('content-type') == 'application/json'
            assert response.json()['name'] == 'CR90 corvette'

        def test_get_nine_starship(self, api_session):
            response = api_session.request(path='starships/9/')
            assert response.status_code == 200
            assert response.headers.get('content-type') == 'application/json'
            assert response.json()['name'] == 'Death Star'

    class TestNegative:
        def test_get_405(self, api_session):
            response = api_session.request(path='starships/', method='POST')
            assert response.status_code == 405
            assert response.json() == RESPONSE_BODY_405

        def test_wrong_query(self, api_session):
            response = api_session.request(path='starships/adsdasd')
            assert response.status_code == 404
            assert response.json() == RESPONSE_BODY_404

