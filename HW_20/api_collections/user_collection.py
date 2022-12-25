from HW_20.api_collections.base_api import BaseAPI
from HW_20.data.user_data import User


class UserAPI(BaseAPI):
    def __init__(self):
        super().__init__()
        self._user_url = '/api/users?page=2'

    def get_user(self, user_id):
        return self.get(f'{self._user_url}/{user_id}')

    def create_user(self, user_data=None):
        if user_data:
            user = User()
            user.update_dict(**user_data)
            json_data = user.get_json()
        else:
            json_data = User().get_json()
        response = self.post(f'{self._user_url}', body=json_data)
        return response
