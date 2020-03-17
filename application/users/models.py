from passlib.hash import pbkdf2_sha256
from application.extensions import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    login_name = db.Column(db.String(64), nullable=False, unique=True)
    password_hash = db.Column(db.Text, nullable=False)
    real_name = db.Column(db.String(128))

    def __init__(self, login_name, password, real_name):
        self.login_name = login_name
        self.password_hash = pbkdf2_sha256.hash(password)
        self.real_name = real_name
