from cid_app import app
from flask import render_template, session, request, redirect,flash
from cid_app.models.admin import Admin
from flask_bcrypt import Bcrypt
from cid_app.utilities.validation import validate
from cid_app.config.validation_checks import registration_checks,login_checks
bcrypt = Bcrypt(app)

@app.route('/admin')
def admin_root():
    if "admin" in session:
        return redirect("/admin/dashboard")
    else:
        return redirect("/admin/login")

@app.route('/admin/login')
def admin_login():
    return render_template('/admin/admin_login.jinja')

@app.route('/admin/login/submit',methods=["POST"])
def admin_login_submit():
    form_data=dict(request.form)
    valid = validate(form_data,login_checks,"login")

    if valid:
        admin = Admin.find_email(form_data=form_data)

        if admin and bcrypt.check_password_hash(admin.password,request.form["password"]):
            admin.password = None
            session["admin"] = {
                "id": admin.id,
                "first_name":admin.first_name,
                "last_name":admin.last_name,
                "email":admin.email,
            }

            return redirect('/admin/dashboard')
        else:
            flash("bad email/password","login_messages")
            return redirect('/admin')
    else:
        return redirect('/admin/login')

@app.route('/admin/register')
def admin_register():
    return render_template('/admin/admin_register.jinja')

@app.route('/admin/register/submit',methods=["POST"])
def admin_register_submit():
    form_data = dict(request.form)

    if validate(form_data,registration_checks,"registration"):
        if form_data["password"] != form_data["confpassword"]:
            flash("Please check if password matches confirmation","registration_error_confpassword")
            return redirect('/admin')
        form_data["password"] = bcrypt.generate_password_hash(form_data["password"])
        session["admin"] = {
            "id": Admin.save(form_data),
            "first_name":form_data["first_name"],
            "last_name":form_data["last_name"],
            "email":form_data["email"],
        }

        return redirect('/admin/dashboard')
    else:
        flash("invalid inputs","register_messages")
        return redirect('/admin/register')

@app.route('/admin/logout')
def admin_logout():
    session.clear()
    return redirect('/admin')