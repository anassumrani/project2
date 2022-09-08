from cgi import test
from urllib import response
from flask import url_for
import age_of_patient
from flask_testing import TestCase
from datetime import date, timedelta
import unittest

class TestBase(TestCase):
    def create_app(self):
        return 
    def setUp(self):
        test_disease = "cancer"
        


class TestViews(TestBase):
    def test_get_disease(self):
        response = self.client.get(url_for('get_disease'))
        self.assert200()
        self.Assert.In(b"cancer")
