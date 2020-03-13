from flask import render_template, request
from application import app
from application.extensions import db
from application.reports.models import Report


@app.route("/reports/new/")
def reports_form():
    return render_template("reports/new.html")


@app.route("/reports/", methods=["POST"])
def reports_create():
    t = Report(request.form.get("title"), request.form.get("summary"),
               request.form.get("priority"))

    db.session().add(t)
    db.session().commit()

    return "hello world!"
