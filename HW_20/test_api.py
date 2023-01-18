from http import HTTPStatus
from HW_20.data.user_data import User
from api_collections.user_collection import UserAPI
import json


def test_get_user_200():
    getresponse = UserAPI().get_user(7)
    assert getresponse.status_code == HTTPStatus.OK, f'Status code is not as expected\nActual ' \
                                                     f'{getresponse.status_code}' \
                                                     f'\nExpected: {HTTPStatus.OK}'


def test_post_user_201():
    postresponse = UserAPI().post_user('morpheus', 'leader')
    assert postresponse.status_code == HTTPStatus.CREATED, f'Status code is not as expected\nActual ' \
                                                           f'{postresponse.status_code}' f'\nExpected: ' \
                                                           f'{HTTPStatus.CREATED}'


def test_put_user_200():
    response = UserAPI().put_user('morpheus', 'zion resident')
    assert response.status_code == HTTPStatus.OK, f'Status code is not as expected\nActual {response.status_code}' \
                                                  f'\nExpected: {HTTPStatus.OK}'


def test_patch_user_200():
    patchresponse = UserAPI().patch_user('morpheus', 'zion resident')
    assert patchresponse.status_code == HTTPStatus.OK, f'Status code is not as expected\nActual ' \
                                                       f'{patchresponse.status_code}' f'\nExpected: {HTTPStatus.OK}'


def test_delete_user_204():
    deleteresponse = UserAPI().delete_user(7)
    assert deleteresponse.status_code == HTTPStatus.NO_CONTENT, f'Status code is not as expected\nActual ' \
                                                                f'{deleteresponse.status_code}' \
                                                                f'\nExpected: {HTTPStatus.NO_CONTENT}'


def test_user_data(create_user):
    expected_user = create_user
    response = UserAPI().get_user(7)
    user_data = json.loads(response.text)
    actual_user = User.from_json(**user_data)
    assert actual_user == expected_user
