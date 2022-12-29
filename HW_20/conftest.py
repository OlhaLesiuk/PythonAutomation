import pytest

from data.user_data import User


@pytest.fixture()
def create_user():
    return User()
