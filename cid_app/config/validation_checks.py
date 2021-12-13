registration_checks = {
	"email": [
		{
			"regex": r"[\w' -]{1,100}",
			"error": "Email can only be a maximum of 100 valid characters",
			"category": "registration_error_email"
		},
		{
			"regex": r"^[\w\d\.-]+@[\w\d\.-]+\.[a-zA-Z]+$",
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

app_checks = {
	"name":[
		{
			"regex": r".{2,100}",
			"error": "Name must be between 2 and 100 characters",
			"category": "app_error_name"
		}
	],
	"callback":[
		{
			"regex": r"https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}(\.[a-zA-Z0-9()]{1,6})*\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)",
			"error": "Must be a valid url",
			"category": "app_error_callback"
		},
		{
			"regex": r".{1,1000}",
			"error": "Must be a max of 100 characters",
			"category": "app_error_callback"
		},
	]
}