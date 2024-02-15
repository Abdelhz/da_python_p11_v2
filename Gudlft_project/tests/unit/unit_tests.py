import sys
import os
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))

from Gudlft_project.server import app, loadClubs

def test_pointsDisplay(client):
    # Test case for points display
    response = client.get('/pointsDisplay', follow_redirects=True)
    assert response.status_code == 200
    clubs = loadClubs()
    for club in clubs:
        assert bytes(club['name'], 'utf-8') in response.data
        assert bytes(str(club['points']), 'utf-8') in response.data