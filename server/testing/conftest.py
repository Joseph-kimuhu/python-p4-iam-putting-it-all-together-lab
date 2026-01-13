#!/usr/bin/env python3

import pytest
from app import app
from models import db

@pytest.fixture(scope='session', autouse=True)
def setup_database():
    with app.app_context():
        db.create_all()
        yield
        db.drop_all()
