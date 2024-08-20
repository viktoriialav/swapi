import json
import logging
from urllib.parse import urljoin

from requests import Session, Response


def json_dumping(cur_dict) -> str:
    return json.dumps(cur_dict, indent=4, ensure_ascii=True)


def pretty_headers(headers):
    if headers:
        return json_dumping(dict(headers))
    else:
        return 'None'


def pretty_body(body: str):
    if body:
        try:
            return json_dumping(json.loads(body))
        except:
            return '\n'.join(list(filter(lambda x: bool(x.split()), body.split('\n'))))
    else:
        return 'None'


def allure_request_logger(function):
    def wrapper(*args, **kwargs):
        response: Response = function(*args, **kwargs)

        logging.info(f'\n\nREQUEST {response.request.method} {response.request.url}\n'
                     f'\nREQUEST HEADERS: \n{pretty_headers(response.request.headers)}\n'
                     f'\nREQUEST BODY: \n{response.request.body}\n'
                     f'\nRESPONSE HEADERS: \n{pretty_headers(response.headers)}\n'
                     f'\nRESPONSE BODY: \n{pretty_body(response.text)}\n')
        return response

    return wrapper


class TestSession(Session):
    def __init__(self, base_url=None):
        super().__init__()
        self.base_url = base_url

    @allure_request_logger
    def request(self, path, method='GET', *args, **kwargs):
        joined_url = urljoin(self.base_url, path)
        return super().request(method, joined_url, *args, **kwargs)
