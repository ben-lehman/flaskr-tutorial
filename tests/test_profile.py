import pytest
from flask import g, session
from flaskr.db import get_db


def test_profile_login_required(client):
    response = client.post('http://localhost/profile/edit')
    assert response.headers['Location'] == 'http://localhost/auth/login'


def test_view_profile(client, auth):
    response = client.get('/profile/1')
    assert b"Hello," in response.data
    assert b"Bio:" in response.data

    auth.login()
    response = client.get('/profile/1')
    assert b"Edit" in response.data


def test_edit_profile(client, auth, app):
    auth.login()
    assert client.get('/profile/edit').status_code == 200
    client.post('/profile/edit', data={'bio': 'New Bio'})

    with app.app_context():
        db = get_db()
        user = db.execute('SELECT * FROM user WHERE id = 1').fetchone()
        assert user['bio'] == 'New Bio'
