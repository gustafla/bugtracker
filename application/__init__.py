from flask import Flask
from application.views import views

app = Flask(__name__)
app.register_blueprint(views)
