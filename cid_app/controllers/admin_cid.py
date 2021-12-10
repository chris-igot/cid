from cid_app import app
from flask import render_template, session, request, redirect,flash
from cid_app.models.app_model import AppModel
from flask_bcrypt import Bcrypt
from cid_app.utilities.validation import validate
from cid_app.config.validation_checks import registration_checks,login_checks
bcrypt = Bcrypt(app)

@app.route('/admin/dashboard')
def dashboard():
    if "admin" in session:
        return render_template('dashboard.jinja',apps=AppModel.find_admin_id(session["admin"]["id"]))
    else:
        return redirect("/admin")

@app.route('/admin/apps/add')
def add_app():
    return render_template("add_app.jinja")
@app.route('/admin/apps/add', methods=["POST"])
def add_app_submit():
    form_data = dict(request.form)
    form_data["admin_id"] = session["admin"]["id"]
    AppModel.save(form_data)
    return redirect("/admin/dashboard")