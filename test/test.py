from cgi import test
from urllib import response
from flask import url_for
from services import app
from services import *
from services import age_of_patient, disease, doctor,service_1
from flask_testing import TestCase
from datetime import date, timedelta
import unittest

class TestBase(TestCase):
    def create_app(self):
        app.config.update()
    def setUp(self):
        test_age = ["20-25","26-30","30+"]
        test_disease = ["stroke","cancer","heart disease"]
        test_doctor = ["dr.basu", "dr.smith","dr.ikong"]
    

class test(TestBase):
     def test_get_age(self):       
        data =  ['20-25']        
        response= self.client.get(url_for('/get/age'))
        self.assert200(response)
        self.assertIs(data, response.data)
        return response