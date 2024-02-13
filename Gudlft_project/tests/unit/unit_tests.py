import pytest
import json
from ...server import app, saveData

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


## 3. BUG: Clubs shouldn't be able to book more than 12 places per competition.

def test_purchasePlaces_more_than_12_places(client):
    response = client.post('/purchasePlaces', data=dict(competition='Spring Festival', club='Simply Lift', places='13'), follow_redirects=True)
    assert b'You cannot book more than 12 places per competition. Please try again.' in response.data

## 5. BUG: Points and places updates are not reflected.

def test_saveData(tmpdir):
    # Create a temporary JSON file in the temporary directory
    clubs_file = tmpdir.join("clubs.json")
    competitions_file = tmpdir.join("competitions.json")

    # Define some initial data
    clubs = [{'name': 'Test Club', 'email': 'TestClub@NewTestClub', 'points': 10}]
    competitions = [{'name': 'Test Competition', 'date': '2025-10-22 13:30:00', 'numberOfPlaces': 10}]

    # Write the initial data to the files
    with open(clubs_file, 'w') as f:
        json.dump({'clubs': clubs}, f)
    with open(competitions_file, 'w') as f:
        json.dump({'competitions': competitions}, f)

    # Define new club and competition
    new_club = {'name': 'New Test Club', 'email': 'NewTestClub@NewTestClub', 'points': 20}
    new_competition = {'name': 'New Test Competition', 'date': '2025-10-22 13:30:00', 'numberOfPlaces': 15}

    # Append new club and competition to the existing data
    clubs.append(new_club)
    competitions.append(new_competition)

    # Call the function with the updated data and the temporary file
    saveData(clubs_file, clubs)
    saveData(competitions_file, competitions)

    # Read the file and check that it contains the updated data
    with open(clubs_file) as f:
        assert json.load(f) == {'clubs': clubs}

    with open(competitions_file) as f:
        assert json.load(f) == {'competitions': competitions}