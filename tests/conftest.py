import os
import pytest

from app import create_app


@pytest.fixture
def app():
    yield create_app()


@pytest.fixture
def client(app):
    print(os.environ.get('REDIS_URL'))
    return app.test_client()


def pytest_generate_tests(metafunc):
    os.environ.setdefault('REDIS_URL', 'redis://localhost:6379/0')
    os.environ.setdefault('GHIBLI_URL', 'https://ghibliapi.herokuapp.com')
