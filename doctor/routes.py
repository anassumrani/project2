from project2 import app
from flask import Response, request
import random

@app.route('/get/doctor', methods=["POST"])
def get_doctor(self):
    data = request.get_json()
    age, disease = data.values()
    doctor = ["dr.basu", "dr.smith","dr.ikong"]
    if age == "20-25" and disease == "heart disease":
        return "dr.basu"
    elif age == "26-30" and disease == "heart disease":
        return "dr.smith"
    else:
        return "dr.ikong"
    if age == "20-25" and disease == "cancer":
        return "dr.smith"
    elif age == "26-30" and disease == "cancer":
        return "dr.ikong"
    else: 
        return "dr.basu"
    if age == "20-25" and disease == "stroke":
        return "dr.ikong"
    elif age == "26-30" and disease == "stoke":
        return "dr.basu"
    else:
        return "dr.smith"