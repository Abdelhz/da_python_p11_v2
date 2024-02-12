import pytest
from ...server import app, loadClubs, loadCompetitions

## 1. ERROR: Entering a unknown email crashes the app
def test_showSummary(client):
    response = client.post('/showSummary', data=dict(email='unknown@email.com'), follow_redirects=True)
    assert response.status_code == 200
    assert b'Club not found. Please try again.' in response.data