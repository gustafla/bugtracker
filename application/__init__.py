from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from application.views import views

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///reports.db"
app.config["SQLALCHEMY_ECHO"] = True
app.register_blueprint(views)

db = SQLAlchemy(app)

db.create_all()
