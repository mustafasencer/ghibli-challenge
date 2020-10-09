import requests
from flask import current_app
from requests import RequestException, HTTPError
import urllib

from utils.error import AppError


class GhibliService:

    def __init__(self):
        self.base_url = current_app.config['GHIBLI_URL']
        self.headers = {
            'Content-Type': 'application/json'
        }

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
