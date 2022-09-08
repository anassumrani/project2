from application import app
from flask import Response
import random


@app.route('/get/age', methods=["GET"])
def get_age():
    age = ["20-25","26-30","30+"]
    randomnum = random.choice(age)
    return Response(randomnum, mimetype="text/plain")