from cid_app import app
import secrets
from flask import render_template, session, request, redirect, flash, jsonify, abort
from cid_app.models.auth_code import AuthCode
from flask_cors import cross_origin
from cid_app.models.user import User
from cid_app.models.app_model import AppModel
from cid_app.utilities.validation import validate


@app.route("/cid/user")
@cross_origin()
def auth():
    # print(request.args)
    if("app_id" in request.args):
        if("user" in session):
            
                site = AppModel.__find_id__(request.args["app_id"])
                if(site):
                    auth_code = AuthCode.generate_code(session["user"]["id"],site.id)
                    # print("auth",session["user"]["id"])
                    return redirect(site.callback+f"?status=0&auth_code={auth_code}")
                else:
                    abort(400,"app_id does not exist")
        else:
            session["request"] = {"app_id":request.args["app_id"]}
            # print("not in session")
            return redirect("/")
    else:
        # print("no website id", request.referrer)
        abort(400,"app_id unavailable")

@app.route("/cid/app")
def auth_app():
    site = AppModel.__find_id__(request.args["app_id"])
    payload = {
        "status":1,
        "token": None
    }
    if("app_id" in request.args and "auth_code" in request.args and "key" in request.args):
        print("\n\nTHIS IS HERE\n\n",request.args)
        auth_code = AuthCode.__find_cols__({"app_id":request.args["app_id"], "code":request.args["auth_code"]})
        site = AppModel.__find_cols__({"id":request.args["app_id"], "key":request.args["key"]})
        print("\n\nTHIS IS also HERE\n\n",auth_code[0],site)
        if((auth_code and site)):
            user = User.get_user(auth_code[0].user_id)
            payload["status"] = 0
            payload["token"] = {
                "id":user["id"],
                "first_name":user["first_name"],
                "last_name":user["last_name"]
            }
    # print("PAYLOAD",payload)
    return jsonify(payload)