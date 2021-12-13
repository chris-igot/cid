from cid_app import app
import secrets
from flask import render_template, session, request, redirect,flash
from cid_app.models.app_model import AppModel
from flask_bcrypt import Bcrypt
from cid_app.utilities.validation import validate
from cid_app.utilities.permission_decorators import admin_access_required, view_edit_access
from cid_app.config.validation_checks import registration_checks,login_checks,app_checks
bcrypt = Bcrypt(app)

@app.route('/admin/dashboard')
@admin_access_required
def dashboard():
    return render_template('dashboard.jinja',apps=AppModel.find_admin_id(session["admin"]["id"]))

@app.route('/admin/apps/add')
@admin_access_required
def add_app():
    return render_template("add_app.jinja")
@app.route('/admin/apps/add', methods=["POST"])
@admin_access_required
def add_app_submit():
    form_data = dict(request.form)
    valid = validate(form_data,app_checks,"app")
    if(valid):
        form_data["admin_id"] = session["admin"]["id"]
        app_id = secrets.token_urlsafe(16)
        form_data["id"] = app_id
        app_key = secrets.token_urlsafe(16)
        form_data["key"] = bcrypt.generate_password_hash(app_key)
        AppModel.save(form_data)
        flash(f"Make sure to copy this key! This is the last and only time you will see this key.",app_id+"gen_key_warning")
        flash(f"<span class='border border-dark rounded p-1'><small class='font-monospace'>{app_key}</small></span>",app_id+"gen_key")
        return redirect("/admin/dashboard")
    else:
        return redirect("/admin/apps/add")

@app.route('/admin/apps/<string:app_id>/edit')
@admin_access_required
@view_edit_access
def edit_app(app_id,app):
    return render_template("edit_app.jinja",app=AppModel.find_id(app_id))

@app.route('/admin/apps/<string:app_id>/edit', methods=["POST"])
@admin_access_required
@view_edit_access
def edit_app_submit(app_id,app):
    form_data = dict(request.form)
    valid = validate(form_data,app_checks,"app")
    if valid:
        form_data["id"] = app_id
        AppModel.save(form_data)
        return redirect("/admin/dashboard")
    else:
        return redirect(f"/admin/apps/{app_id}/edit")

@app.route('/admin/apps/<string:app_id>/genkeyask')
@admin_access_required
@view_edit_access
def generate_new_key_ask(app_id,app):

    flash(f"Are you sure you want to generate a new key?<br><a href='/admin/apps/{app_id}/genkey' class='btn btn-danger'>confirm</a>",app_id+"gen_key_confirm")
    flash(f"",app_id+"gen_key")
    return redirect(f"/admin/dashboard")

@app.route('/admin/apps/<string:app_id>/genkey')
@admin_access_required
@view_edit_access
def generate_new_key(app_id,app):
    app_key = secrets.token_urlsafe(16)
    form_data = {
        "id":app_id,
        "key": bcrypt.generate_password_hash(app_key)
    }
    AppModel.save(form_data)
    flash(f"Make sure to copy this key! This is the last and only time you will see this key.",app_id+"gen_key_warning")
    flash(f"<span class='border border-dark rounded p-1'><small class='font-monospace'>{app_key}</small></span>",app_id+"gen_key") 
    return redirect("/admin/dashboard")