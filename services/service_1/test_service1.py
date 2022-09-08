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
        test_age = "20-25"
        test_disease = "cancer"
        


class TestViews(TestBase):
    def test_get_data(self):
        response = self.client.get(url_for('get_data'))
        self.assert200()
        self.Assert.In(b'test_age:"20-25", test_disease:"cancer"', response.data)
