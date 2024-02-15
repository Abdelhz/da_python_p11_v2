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

## 2. BUG: Clubs should not be able to use more than their points Available or competition places available.
def test_purchasePlaces(client, clubs, competitions):
    #response = client.post('/purchasePlaces', data=dict(competition='Trials of Osiris', club='Iron lords', places='1'), follow_redirects=True)
    response = client.post('/purchasePlaces', data=dict(competition=competitions[4]['name'], club=clubs[3]['name'], places='1'), follow_redirects=True)
    assert 'Great-booking complete!' in response.get_data(as_text=True)

def test_purchasePlaces_no_enough_points(client, clubs, competitions):
    #response = client.post('/purchasePlaces', data=dict(competition='Fall Classic', club='Iron lords', places='10'), follow_redirects=True)
    response = client.post('/purchasePlaces', data=dict(competition=competitions[1]['name'], club=clubs[3]['name'], places='10'), follow_redirects=True)
    assert 'Not enough points Available to the club. Please try again.' in response.get_data(as_text=True)

def test_purchasePlaces_no_enough_places(client, clubs, competitions):
    #response = client.post('/purchasePlaces', data=dict(competition='Blazing fire', club='Simply Lift', places='12'), follow_redirects=True)
    response = client.post('/purchasePlaces', data=dict(competition=competitions[3]['name'], club=clubs[0]['name'], places='12'), follow_redirects=True)
    print(response.get_data(as_text=True))  # print the response data
    assert 'Not enough places available in the competition. Please try again.' in response.get_data(as_text=True)

def test_purchasePlaces_invalid_places(client, clubs, competitions):
    #response = client.post('/purchasePlaces', data=dict(competition='Fall Classic', club='Simply Lift', places='invalid'), follow_redirects=True)
    response = client.post('/purchasePlaces', data=dict(competition=competitions[1]['name'], club=clubs[0]['name'], places='invalid'), follow_redirects=True)
    assert 'Invalid value for number of places required. Please try again.' in response.get_data(as_text=True)

## 3. BUG: Clubs shouldn't be able to book more than 12 places per competition
def test_purchasePlaces_more_than_12_places(client, clubs, competitions):
    #response = client.post('/purchasePlaces', data=dict(competition='Spring Festival', club='Simply Lift', places='13'), follow_redirects=True)
    response = client.post('/purchasePlaces', data=dict(competition=competitions[0]['name'], club=clubs[0]['name'], places='13'), follow_redirects=True)
    print(response.get_data(as_text=True))  # print the response data
    assert 'You cannot book more than 12 places per competition. Please try again.' in response.get_data(as_text=True)
