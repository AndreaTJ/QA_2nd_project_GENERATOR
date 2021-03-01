from unittest.mock import patch
from flask import url_for, request
from flask_testing import TestCase

from app import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):
    def test_random_number(self):
        numbers= [b"100", b"10", b"200", b"34", b"500", b"780", b"300", b"430", b"3", b"0.4"]
        response = self.client.get(url_for("prizes"))
        self.assertIn(response.data, numbers)
