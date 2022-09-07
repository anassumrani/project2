from cgi import test
from urllib import response
from flask import url_for
from services import app
from services import *
from services import age_of_patient, disease, doctor,service_1
from flask_testing import TestCase
from datetime import date, timedelta

def setup(self):
    test_age_of_patient= age_of_patient(age="20-25")
    test_disease = disease(disease="cancer")
    test_doctor = doctor(doctor="dr.basu")
    