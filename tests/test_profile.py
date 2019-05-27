import pytest
from flask import g, session
from flaskr.db import get_db


@pytest.mark.parametrize('path', (
    '/profile'
    '/profile/edit'
))
def test_profile_login_required(client, path):
    
