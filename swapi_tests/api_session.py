from urllib.parse import urljoin

from requests import Session


class TestSession(Session):
    def __init__(self, base_url=None):
        super().__init__()
        self.base_url = base_url

    def request(self, path, method='GET', *args, **kwargs):
        joined_url = urljoin(self.base_url, path)
        return super().request(method, joined_url, *args, **kwargs)
