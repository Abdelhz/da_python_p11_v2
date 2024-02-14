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