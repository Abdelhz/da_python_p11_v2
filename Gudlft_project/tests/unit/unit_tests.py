import sys
import os
import pytest
import json

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))

from Gudlft_project.server import app, saveData

## 2. BUG: Clubs should not be able to use more than their points Available or competition places available.
def test_purchasePlaces(client, clubs, competitions):
    #response = client.post('/purchasePlaces', data=dict(competition='Trials of Osiris', club='Iron lords', places='1'), follow_redirects=True)
    response = client.post('/purchasePlaces', data=dict(competition=competitions[4]['name'], club=clubs[3]['name'], places='1'), follow_redirects=True)
    #print(response.get_data(as_text=True))  # print the response data
    assert 'Great-booking complete!' in response.get_data(as_text=True)

def test_purchasePlaces_no_enough_points(client, clubs, competitions):
    #response = client.post('/purchasePlaces', data=dict(competition='Fall Classic', club='Iron lords', places='10'), follow_redirects=True)
    response = client.post('/purchasePlaces', data=dict(competition=competitions[1]['name'], club=clubs[3]['name'], places='10'), follow_redirects=True)
    print(response.get_data(as_text=True))  # print the response data
    assert 'Not enough points Available to the club. Please try again.' in response.get_data(as_text=True)

def test_purchasePlaces_no_enough_places(client, clubs, competitions):
    #response = client.post('/purchasePlaces', data=dict(competition='Blazing fire', club='Simply Lift', places='12'), follow_redirects=True)
    response = client.post('/purchasePlaces', data=dict(competition=competitions[3]['name'], club=clubs[0]['name'], places='12'), follow_redirects=True)
    #print(response.get_data(as_text=True))  # print the response data
    assert 'Not enough places available in the competition. Please try again.' in response.get_data(as_text=True)

def test_purchasePlaces_invalid_places(client, clubs, competitions):
    #response = client.post('/purchasePlaces', data=dict(competition='Fall Classic', club='Simply Lift', places='invalid'), follow_redirects=True)
    response = client.post('/purchasePlaces', data=dict(competition=competitions[1]['name'], club=clubs[0]['name'], places='invalid'), follow_redirects=True)
    #print(response.get_data(as_text=True))  # print the response data
    assert 'Invalid value for number of places required. Please try again.' in response.get_data(as_text=True)


## 3. BUG: Clubs shouldn't be able to book more than 12 places per competition
def test_purchasePlaces_more_than_12_places(client, clubs, competitions):
    #response = client.post('/purchasePlaces', data=dict(competition='Spring Festival', club='Simply Lift', places='13'), follow_redirects=True)
    response = client.post('/purchasePlaces', data=dict(competition=competitions[0]['name'], club=clubs[0]['name'], places='13'), follow_redirects=True)
    #print(response.get_data(as_text=True))  # print the response data
    assert 'You cannot book more than 12 places per competition. Please try again.' in response.get_data(as_text=True)

## 5. BUG: Points and places updates are not reflected.
'''
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
'''