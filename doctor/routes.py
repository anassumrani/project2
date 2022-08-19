from project2 import app
from flask import Response
import random

@app.route('/get/doctor', methods="GET")
def get_doctor(self):
    doctor = ["dr.basu", "dr.smith","dr.ikong"]:
    if age == "20-25" and disease == "heart disease":
        return doctor("dr.basu")
    elif age == "26-30" and disease == "heart disease":
        return doctor("dr.smith")
    else return doctor("dr.ikong")
    if age == "20-25" and disease == "cancer":
        return doctor("dr.smith")
    elif age == "26-30" and disease == "cancer":
        return doctor("dr.ikong")
    else return doctor("dr.basu")
    if age == "20-25" and disease == "stroke":
        return doctor("dr.ikong")
    elif age == "26-30" and disease == "stoke":
        return doctor("dr.basu")
    else return doctor("dr.smith")