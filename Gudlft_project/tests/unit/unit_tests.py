import pytest
from ...server import app, loadClubs, loadCompetitions

## 1. ERROR: Entering a unknown email crashes the app
def test_showSummary(client):
    response = client.post('/showSummary', data=dict(email='unknown@email.com'), follow_redirects=True)
    assert b'Club not found. Please try again.' in response.data

def test_book(client):
    response = client.get('/book/unknown_competition/unknown_club', follow_redirects=True)
    assert b'Something went wrong-please try again' in response.data