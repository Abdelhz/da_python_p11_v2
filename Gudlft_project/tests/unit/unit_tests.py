import pytest
from ...server import app

## 1. ERROR: Error handling if competition or club not found in book route
def test_book(client):
    response = client.get('/book/unknown_competition/unknown_club', follow_redirects=True)
    assert response.status_code == 200
    assert b'Something went wrong-please try again' in response.data