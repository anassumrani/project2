from crypt import methods
from urllib import response
from project2 import app
from flask import Response, request, redirect, url_for, render_template
import random
import requests


@app.route('/', methods=["GET"])
def home_page(self):
    return render_template('form.html')


@app.route('/get/data_age', methods=["GET"])
def get_data_age(self):
    age = requests.get()
    disease = requests.get()
    doctor = response.text()
    

    