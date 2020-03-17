from flask import render_template, request, redirect, url_for
from application import app
from application.extensions import db
from application.users.models import User


@app.route("/users/new/")
def users_form():
    return render_template("users/new.html")


@app.route("/users/", methods=["POST"])
def users_create():
    form = request.form
    u = User(form.get("login_name"), form.get("password"),
             form.get("real_name"))

    db.session().add(u)
    db.session().commit()

    return redirect(url_for("index"))
