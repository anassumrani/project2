from flask import Flask
from os import getenv

app = Flask(__name__)
import application.routes as routes 