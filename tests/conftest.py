import pytest

from swapi_tests.api_session import TestSession


@pytest.fixture(scope='session')
def api_session():
    session = TestSession()
    session.base_url = 'https://swapi.dev/api/'
    session.headers.update({'User-Agent': 'Opera'})
    return session


@pytest.fixture(scope='session')
def api_wookiee_session():
    session = TestSession()
    session.base_url = 'https://swapi.dev/api/'
    session.headers.update({'User-Agent': 'Opera'})
    session.params = {'format': 'wookiee'}
    return session


@pytest.fixture(scope='function')
def api_destruction_session():
    session = TestSession()
    session.base_url = 'https://swapi.dev/api/'
    session.headers.update({'User-Agent': 'Opera'})
    return session
