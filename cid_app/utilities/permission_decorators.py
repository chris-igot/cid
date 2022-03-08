from functools import wraps
from flask import session,redirect, flash
from cid_app.models.app_model import AppModel

def login_required(f):
	@wraps(f)
	def decorated_function(*args, **kwargs):
		if 'user' not in session:
			flash("You must log in first","login_messages")
			return redirect('/')
		return f(*args, **kwargs)
	return decorated_function

def admin_access_required(f):
	@wraps(f)
	def decorated_function(*args, **kwargs):
		if 'admin' not in session:
			flash("You must log in first","login_messages")
			return redirect('/admin')
		return f(*args, **kwargs)
	return decorated_function

def view_edit_access(f):
	@wraps(f)
	def decorated_function(*args, **kwargs):
		kwargs["app"] = AppModel.find_id(kwargs["app_id"])
		if not kwargs["app"]:
			app_id = kwargs["app_id"]
			flash(f"This app_id {app_id} does not exist","access_messages")
			return redirect(f'/admin/dashboard')
		if session["admin"]["id"] != kwargs["app"].admin_id: # type: ignore
			flash(f"You are not authorized to view/edit this app","access_messages")
			return redirect(f'/admin/dashboard')
		return f(*args, **kwargs)
	return decorated_function