from flask import Flask
from .extensions import db

import application.reports.models # noqa

app = Flask(__name__.split('.')[0])

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///reports.db"
app.config["SQLALCHEMY_ECHO"] = True
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

with app.app_context():
    db.create_all()

import application.views # noqa
import application.reports.views # noqa
