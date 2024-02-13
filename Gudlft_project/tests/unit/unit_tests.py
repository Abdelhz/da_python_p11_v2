import pytest
from ...server import app

def test_pointsDisplay(client):
    # Test case for points display
    response = client.get('/pointsDisplay', follow_redirects=True)
    assert response.status_code == 200
    for club in clubs:
        assert bytes(club['name'], 'utf-8') in response.data
        assert bytes(str(club['points']), 'utf-8') in response.data