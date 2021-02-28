from unittest.mock import patch
from flask import url_for, request
from flask_testing import TestCase

from app import app, db, Duo

class TestBase (TestCase):
    def create_app (self): 
        app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///",
        TESTING = True)

        return app
        
    def setUp (self): 
        db.create_all()
        db.session.add (Duo (country= "Mexico", money = "5000"))
        db.session.commit()

        
 
    def tearDown (self):
        db.session.remove()
        db.drop_all()


class Test_Response(TestBase):
    def test_request(self):
        with patch("requests.get") as g:
            g.return_value.text = "{'Rome': '125000.0'}"

            response = self.client.get(url_for("hello_internet"))
            self.assertIn(b"Rome", response.data)

    def test_saving_records(self):
        db.create_all()
        db.session.add (Duo (country= "Paris", money = "5000"))
        db.session.commit()

        
        

