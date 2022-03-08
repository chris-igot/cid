from cid_app import app
from flask import render_template, session, request, redirect,flash
from cid_app.models.user import User
from flask_bcrypt import Bcrypt
from cid_app.utilities.validation import validate
from cid_app.utilities.permission_decorators import login_required
from cid_app.config.validation_checks import registration_checks,login_checks
bcrypt = Bcrypt(app)

@app.route('/')
def user_root():
    if "user" in session:
        return redirect("/welcome")
    else:
        return redirect("/login")

@app.route('/login')
def user_login():
    return render_template('user/login.jinja')

@app.route('/welcome')
@login_required
def welcome():
    return render_template('user/user_status.jinja')

@app.route('/login/submit',methods=["POST"])
def user_login_submit():
    form_data=dict(request.form)
    valid = validate(form_data,login_checks,"login")

    if valid:
        user = User.find_email(form_data)

        if user and  bcrypt.check_password_hash(user.password,request.form["password"]):
            user.password = None
            session["user"] = {
                "id": user.id,
                "first_name":user.first_name,
                "last_name":user.last_name,
                "email":user.email,
            }

            if "request" in session:
                app_id = session["request"]["app_id"]

                del session["request"]
                return redirect("/cid/user?app_id="+app_id)
            else:
                return redirect('/welcome')
        else:
            flash("bad email/password","login_messages")
            return redirect('/login')
    else:
        return redirect('/login')

@app.route('/register')
def user_register():
    return render_template('user/register.jinja')

@app.route('/register/submit',methods=["POST"])
def user_register_submit():
    form_data = dict(request.form)

    if validate(form_data,registration_checks,"registration"):
        if form_data["password"] != form_data["confpassword"]:
            flash("Please check if password matches confirmation","registration_error_confpassword")
            return redirect('/')
        form_data["password"] = bcrypt.generate_password_hash(form_data["password"])
        session["user"] = {
            "id": User.save(form_data),
            "first_name":form_data["first_name"],
            "last_name":form_data["last_name"],
            "email":form_data["email"],
        }

        if "request" in session:
            app_id = session["request"]["app_id"]

            del session["request"]
            return redirect("/cid/user?app_id="+app_id)
        else:
            return redirect('/welcome')
    else:
        flash("invalid inputs","register_messages")
        return redirect('/register')

@app.route('/logout')
def user_logout():
    session.clear()
    if("cb" in request.args):
        return redirect(request.args["cb"])
    else:
        return redirect('/')