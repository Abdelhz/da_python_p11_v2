import sys
import os
import pytest
import json
from flask import template_rendered
from contextlib import contextmanager

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))

from Gudlft_project.server import app, saveData, loadClubs, loadCompetitions

@contextmanager
def captured_templates(app):
    recorded = []
    def record(sender, template, context, **extra):
        recorded.append((template, context))
    template_rendered.connect(record, app)
    try:
        yield recorded
    finally:
        template_rendered.disconnect(record, app)

def test_index(client):
    with captured_templates(app) as templates:
        response = client.get('/')
        assert response.status_code == 200
        assert len(templates) == 1
        template, context = templates[0]
        assert template.name == 'index.html'

def test_showSummary(monkeypatch, client, clubs, competitions):
    monkeypatch.setattr('Gudlft_project.server.loadClubs', lambda: clubs)
    monkeypatch.setattr('Gudlft_project.server.loadCompetitions', lambda: competitions)
    with captured_templates(app) as templates:
        response = client.post('/showSummary', data=dict(email=clubs[0]['email']), follow_redirects=True)
        assert response.status_code == 200
        assert len(templates) == 1
        template, context = templates[0]
        assert template.name == 'welcome.html'
        assert context['club'] == clubs[0]
        assert context['competitions'] == competitions

def test_book(monkeypatch, client, clubs, competitions):
    monkeypatch.setattr('Gudlft_project.server.loadClubs', lambda: clubs)
    monkeypatch.setattr('Gudlft_project.server.loadCompetitions', lambda: competitions)
    with captured_templates(app) as templates:
        response = client.get(f'/book/{competitions[0]["name"]}/{clubs[0]["name"]}', follow_redirects=True)
        assert response.status_code == 200
        assert len(templates) == 1
        template, context = templates[0]
        assert template.name == 'booking.html'
        assert context['club'] == clubs[0]
        assert context['competition'] == competitions[0]

def test_pointsDisplay(monkeypatch, client, clubs, competitions):
    monkeypatch.setattr('Gudlft_project.server.loadClubs', lambda: clubs)
    monkeypatch.setattr('Gudlft_project.server.loadCompetitions', lambda: competitions)
    with captured_templates(app) as templates:
        response = client.get('/pointsDisplay', follow_redirects=True)
        assert response.status_code == 200
        assert len(templates) == 1
        template, context = templates[0]
        assert template.name == 'points_display.html'
        assert context['clubs'] == clubs