from crypt import methods
from urllib import response
from application import app
from flask import Response, request, redirect, url_for, render_template
import random
import requests


@app.route('/get/data', methods=["GET"])
def get_data():
    age = requests.get("http://age:5001/get/age")
    disease = requests.get("http://disease:5002/get/disease")
    doctor = requests.post("http://doctor:5003/get/doctor", json={"age": age.text, "disease": disease.text })
    return render_template('index.html', doctor = doctor.text)
    

    
   