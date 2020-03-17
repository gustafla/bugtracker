from flask import render_template, request, redirect, url_for
from application import app
from application.extensions import db
from application.reports.models import Report


@app.route("/reports/", methods=["GET"])
def reports_index():
    return render_template("reports/list.html", reports = Report.query.all())


@app.route("/reports/new/")
def reports_form():
    return render_template("reports/new.html")


@app.route("/reports/", methods=["POST"])
def reports_create():
    form = request.form
    r = Report(form.get("title"), form.get("description"), form.get("priority"))

    db.session().add(r)
    db.session().commit()

    return redirect(url_for("reports_index"))
