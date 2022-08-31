from urllib import response
from project2 import app
from flask import Response, request
import random
import requests

@app.route('/get/data_age', methods=["GET"])
def get_data_age(self):
    age = requests.get()
    disease = requests.get()
    doctor = response.text()

    