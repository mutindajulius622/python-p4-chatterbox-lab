#!/usr/bin/env python3

import pytest
from app import app
from models import db
from seed import make_messages

@pytest.fixture(scope='session', autouse=True)
def setup_database():
    '''Setup test database before running tests'''
    with app.app_context():
        db.create_all()
        make_messages()
        yield
        db.drop_all()

def pytest_itemcollected(item):
    par = item.parent.obj
    node = item.obj
    pref = par.__doc__.strip() if par.__doc__ else par.__class__.__name__
    suf = node.__doc__.strip() if node.__doc__ else node.__name__
    if pref or suf:
        item._nodeid = ' '.join((pref, suf))