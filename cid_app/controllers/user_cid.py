from cid_app import app
import secrets
from flask import render_template, session, request, redirect, flash, jsonify, abort
from cid_app.models.auth_code import AuthCode
from flask_cors import cross_origin
from flask_bcrypt import Bcrypt
from cid_app.models.user import User
from cid_app.models.app_model import AppModel
from cid_app.utilities.validation import validate
from cid_app.config.url_parameter_checks import cid_user, cid_app
bcrypt = Bcrypt(app)


@app.route("/cid/user")
@cross_origin()
def auth():
    data = request.args
    valid = validate(data,cid_user,"cid_app",func=print)
    if(valid):
        if("user" in session):
                site = AppModel.find_id(data["app_id"])

                if(site):
                    auth_code = AuthCode.generate_code(session["user"]["id"],site.id)
                    return redirect(site.callback+f"?auth_code={auth_code}")
                else:
                    abort(400,"app_id does not exist")
        else:
            session["request"] = {"app_id":data["app_id"]}
            return redirect("/")
    else:
        abort(400,"app_id unavailable")

@app.route("/cid/app")
def auth_app():
    payload = {
        "status":1,
        "token": None
    }
    data = request.args
    validation_result = {}
    valid = validate(data,cid_app,"cid_app",func=print,result=validation_result)
    if(valid):
        site = AppModel.find_id(data["app_id"])
        auth_code = AuthCode.find_code(data["auth_code"],data["app_id"])

        if((auth_code and site and auth_code.status == "new" and bcrypt.check_password_hash(site.key,data["key"]))):
            user = User.find_id(auth_code.user_id)
            user.password = None
            payload["status"] = 0
            payload["token"] = {
                "id":user.id,
                "first_name":user.first_name,
                "last_name":user.last_name,
                "email":user.email
            }
            updated_data = {
                "code": data["auth_code"],
                "user_id":user.id,
                "app_id": data["app_id"],
                "status": "used"
            }
            AuthCode.save(updated_data)
    else:
        payload["validation_result"] = validation_result

    return jsonify(payload)