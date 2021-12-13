from cid_app import app
from cid_app.controllers import user_login
from cid_app.controllers import user_cid
from cid_app.controllers import admin_login
from cid_app.controllers import admin_cid


@app.errorhandler(404)
def bad_path(err):
	return "This page does not exist!!"

if __name__ == "__main__":
	app.run(debug=True, port=5000,host="192.168.0.103")