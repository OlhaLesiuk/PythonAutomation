from http import HTTPStatus
from HW_20.data.user_data import User
from api_collections.user_collection import UserAPI
import json


def test_get_user_200():
    response = UserAPI().get_user(7)
    assert response.status_code == HTTPStatus.OK, f'Status code is not as expected\nActual {response.status_code}' \
                                                  f'\nExpected: {HTTPStatus.OK}'


def test_user_data(create_user):
    expected_user = create_user
    response = UserAPI().get_user(7)
    user_data = json.loads(response.text)
    actual_user = User.from_json(**user_data)
    assert actual_user == expected_user
