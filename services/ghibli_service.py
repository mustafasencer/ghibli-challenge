import requests
from requests import RequestException
import urllib

from utils.error import AppError


class GhibliService:

    def init_app(self, app):
        self.base_url = app.config.get('GHIBLI_URL')
        app.extensions[self.config_prefix.lower()] = self

    def __init__(self, config_prefix='GHIBLI'):
        self.base_url = None
        self.headers = {
            'Content-Type': 'application/json'
        }
        self.config_prefix = config_prefix

    def _fetch(self, endpoint):
        try:
            response = requests.get(f'{self.base_url}/{endpoint}').json()
        except RequestException as ex:
            raise AppError(
                status=400,
                err_code='errors.ghibliApiError',
                err_msg=f'{ex.request.body}',
                reason=f'{ex.request.url}'
            )
        except ConnectionError as ex:
            raise AppError(
                status=400,
                err_code='errors.ghibliApiConnectionError',
                err_msg=f'{ex[:1000]}'
            )
        return response

    def list(self, endpoint, query_params):
        query_string = urllib.parse.urlencode(query_params)
        endpoint = f'{endpoint}?{query_string}'
        return self._fetch(endpoint)

    def get_by_id(self, endpoint, _id):
        endpoint = f'{endpoint}/{_id}'
        return self._fetch(endpoint)
