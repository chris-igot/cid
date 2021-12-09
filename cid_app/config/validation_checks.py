registration_checks = {
	"email": [
		{
			"regex": r"[\w' -]{1,100}",
			"error": "Email can only be a maximum of 100 valid characters",
			"category": "registration_error_email"
		},
		{
			"regex": r"^[\w\.-]+@[\w\.-]+\.[a-zA-Z]+$",
			"error": "Please enter valid email address",
			"category": "registration_error_email"
		}
	],
	"first_name": [
		{
			"regex": r"[\w' -]{3,100}",
			"error": "First Name must be between 3 and 100 valid characters",
			"category": "registration_error_first_name"
		}
	],
	"last_name": [
		{
			"regex": r"[\w' -]{3,100}",
			"error": "Last Name must be between 3 and 100 valid characters",
			"category": "registration_error_last_name"
		}
	],
	"password": [
		{
			"regex": r".{8,100}",
			"error": "Password must be between 8 and 100 characters",
			"category": "registration_error_password"
		}
	]
}
login_checks = {
	"email": [
		{
			"regex": r"[\w' -]{1,100}",
			"error": "Please enter an email address",
			"category": "login_error_email"
		}
	],
	"password": [
		{
			"regex": r".{1,100}",
			"error": "Please enter an email address",
			"category": "login_error_password"
		}
	]
}

pie_checks = {
	"name":[
		{
			"regex": r".{1,100}",
			"error": "Name must be between 2 and 200 characters",
			"category": "pie_error_name"
		}
	],
	"filling":[
		{
			"regex": r".{1,100}",
			"error": "Filling must be between 20 and 1000 characters",
			"category": "pie_error_filling"
		}
	],
	"crust":[
		{
			"regex": r".{1,100}",
			"error": "Crust must be between 20 and 10000 characters",
			"category": "pie_error_crust"
		}
	]
}