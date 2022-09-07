from crypt import methods
from urllib import response
from application import app
from flask import Response, request, redirect, url_for, render_template
import random
import requests


@app.route('/', methods=["GET"])
def home_page(self):
    return render_template('form.html')


@app.route('/get/data', methods=["GET"])
def get_data(self):
    age = requests.get("http://age_of_patient:5000/get/age")
    disease = requests.get("http://disease:5000/get/disease")
    doctor = requests.post("http://doctor:5000//get/doctor")
    

    