cid_user = {
    "app_id":[
		{
			"regex": r"[\w\d_-]+",
			"error": "app_id must be present",
			"category": "cid_user_error_app_id"
		}
	]

}

cid_app = {
    "app_id":[{
        "regex": r"[\w\d_-]+",
        "error": "app_id must be present",
        "category": "cid_app_error_app_id"
    }],
    "auth_code":[{
        "regex": r"[\w\d_-]+",
        "error": "auth_code must be present",
        "category": "cid_app_error_auth_code"
    }],
    "key":[{
        "regex": r"[\w\d_-]+",
        "error": "key must be present",
        "category": "cid_app_error_key"
    }]
}
