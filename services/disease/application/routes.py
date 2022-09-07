from application import app
from flask import Response
import random
import application

@app.route("/get/disease", methods=["GET"])
def get_disease(self):
    disease = ["stroke","cancer","heart disease"]
    randomnum = random.choice(disease)
    return Response(randomnum, mimetype="text/plain")