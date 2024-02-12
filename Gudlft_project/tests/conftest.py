import pytest
from server import app as flask_app  # import your Flask application

@pytest.fixture
def client():
    flask_app.config['TESTING'] = True
    with flask_app.test_client() as client:
        yield client