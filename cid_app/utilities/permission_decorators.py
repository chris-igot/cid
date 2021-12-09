from functools import wraps
from flask import session,redirect, flash
# from pypiesderby_app.models.pie import Pie

def login_required(f):
	@wraps(f)
	def decorated_function(*args, **kwargs):
		# print(session.user_id)
		if 'user_id' not in session:
			flash("You must log in first","login_messages")
			return redirect('/')
		return f(*args, **kwargs)
	return decorated_function

# def edit_authorization_required(f):
# 	@wraps(f)
# 	def decorated_function(*args, **kwargs):
# 		# print("ARGS",args)
# 		# print("KWARGS",kwargs)
# 		kwargs["pie"] = Pie.get_one(kwargs["pie_id"])
# 		if session["user_id"] != kwargs["pie"].user.id: # type: ignore
# 			flash("You are not authorized to edit this pie","edit_messages")
# 			return redirect(f'/show/{kwargs["pie_id"]}')
# 		return f(*args, **kwargs)
# 	return decorated_function