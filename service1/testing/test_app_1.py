from unittest.mock import patch
from flask import url_for, request
from flask_testing import TestCase

from app import app

class TestBase (TestCase):
    def create_app (self): 
        app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///",
        TESTING = True)

        return app




        
        

