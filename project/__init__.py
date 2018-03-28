from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, static_folder='static')
app.config.from_object('setting')

db = SQLAlchemy(app)

from . import controller

controller.initialize()
