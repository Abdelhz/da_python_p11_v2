import sys
import os
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))

from Gudlft_project.server import app

## 1. ERROR: Entering a unknown email crashes the app
def test_showSummary(client):
    response = client.post('/showSummary', data=dict(email='unknown@email.com'), follow_redirects=True)
    assert response.status_code == 200
    assert b'Club not found. Please try again.' in response.data

## 1.2. ERROR: Error handling if competition or club not found in book route
def test_book(client):
    response = client.get('/book/unknown_competition/unknown_club', follow_redirects=True)
    assert response.status_code == 200
    assert b'Something went wrong-please try again' in response.data
import pytest
from ...server import app

## 2. BUG: Clubs should not be able to use more than their points Available or competition places available.
def test_purchasePlaces(client):
    response = client.post('/purchasePlaces', data=dict(competition='Fall Classic', club='Iron Temple', places='1'), follow_redirects=True)
    assert b'Great-booking complete!' in response.data

def test_purchasePlaces_no_enough_points(client):
    response = client.post('/purchasePlaces', data=dict(competition='Fall Classic', club='Iron Temple', places='10'), follow_redirects=True)
    assert b'Not enough points Available to the club. Please try again.' in response.data

def test_purchasePlaces_no_enough_places(client):
    response = client.post('/purchasePlaces', data=dict(competition='Fall Classic', club='Simply Lift', places='13'), follow_redirects=True)
    assert b'Not enough places to the competition. Please try again.' in response.data

def test_purchasePlaces_invalid_places(client):
    response = client.post('/purchasePlaces', data=dict(competition='Fall Classic', club='Simply Lift', places='invalid'), follow_redirects=True)
    assert b'Invalid value for number of places. Please try again.' in response.data
