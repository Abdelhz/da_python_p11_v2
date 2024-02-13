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


## 3. BUG: Clubs shouldn't be able to book more than 12 places per competition
def test_purchasePlaces_more_than_12_places(client):
    response = client.post('/purchasePlaces', data=dict(competition='Spring Festival', club='Simply Lift', places='13'), follow_redirects=True)
    assert b'You cannot book more than 12 places per competition. Please try again.' in response.data