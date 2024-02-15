import pytest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from Gudlft_project.server import app as flask_app  # import your Flask application

@pytest.fixture
def client():
    flask_app.config['TESTING'] = True
    with flask_app.test_client() as client:
        yield client

@pytest.fixture
def clubs():
    return [
        {"name":"Simply Lift", "email":"john@simplylift.co", "points":"13"},
        {"name":"Iron Temple", "email": "admin@irontemple.com", "points":"4"},
        {"name":"She Lifts", "email": "kate@shelifts.co.uk", "points":"12"},
        {"name":"Iron lords", "email": "Ironlords@Ironlords.co.uk", "points":"6"}
    ]

@pytest.fixture
def competitions():
    return [
        {"name": "Spring Festival", "date": "2025-03-27 10:00:00", "numberOfPlaces": "25"},
        {"name": "Fall Classic", "date": "2025-10-22 13:30:00", "numberOfPlaces": "13"},
        {"name": "Hearts OF stone", "date": "2020-10-22 13:30:00", "numberOfPlaces": "13"},
        {"name": "Blazing fire", "date": "2025-10-22 13:30:00", "numberOfPlaces": "10"},
        {"name": "Trials of Osiris", "date": "2025-10-22 13:30:00", "numberOfPlaces": "13"},
        {"name": "The Maw Of Lorkhaj", "date": "2025-10-22 13:30:00", "numberOfPlaces": "13"}
    ]