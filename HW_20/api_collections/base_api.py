import requests

from HW_20.config import BASE_URL


class BaseAPI:
    def __init__(self):
        self.__base_url = BASE_URL
        self._headers = {'Content-Type': 'application/json'}
        self.__request = requests

    def get(self, url, headers=None, params=None):
        print('FROM Base API')
        if headers is None:
            headers = self._headers
        response = self.__request.get(f'{self.__base_url}/{url}', params=params, headers=headers)
        return response

    def post(self, url, body=None, headers=None, params=None):
        if headers is None:
            headers = self._headers
        response = self.__request.post(f'{self.__base_url}/{url}', json=body, headers=headers, params=params)
        return response

    def put(self, url, body=None, headers=None, params=None):
        if headers is None:
            headers = self._headers
        response = self.__request.put(f'{self.__base_url}/{url}', json=body, headers=headers, params=params)
        return response

    def patch(self, url, body=None, headers=None, params=None):
        if headers is None:
            headers = self._headers
        response = self.__request.patch(f'{self.__base_url}/{url}', json=body, headers=headers, params=params)
        return response

    def delete(self, url, body=None, headers=None, params=None):
        if headers is None:
            headers = self._headers
        response = self.__request.delete(f'{self.__base_url}/{url}', json=body, headers=headers, params=params)
        return response
