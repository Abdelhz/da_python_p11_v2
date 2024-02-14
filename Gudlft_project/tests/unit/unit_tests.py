import sys
import os
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))

from Gudlft_project.server import app

## 1.2. ERROR: Error handling if competition or club not found in book route.
def test_book(client):
    response = client.get('/book/unknown_competition/unknown_club', follow_redirects=True)
    assert response.status_code == 200
    assert b'Something went wrong-please try again' in response.data

## 4. BUG: Booking in past competitions.
def test_booking_past_competition(client):
    club_name = "She Lifts"
    OutDated_competition_name = "Hearts OF stone"

    response = client.get(f'/book/{OutDated_competition_name}/{club_name}')
    assert "This competition is outdated, you cannot book places for it. Please choose another competition." in response.get_data(as_text=True)