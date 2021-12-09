from flask import flash
import re

def validate(form_data,checks,form_name="form",strict=True):
	valid = True
	for key, val in checks.items():
		if key in form_data:
			for check in val:
				regex = re.compile(check["regex"])
				if not regex.match(form_data[key]):
					valid = False
					print(check["error"],check["category"])
					flash(check["error"],check["category"])
		elif strict and key not in form_data:
			valid = False
			print(f"Field {key} not submitted",form_name+"_messages")
			flash(f"Field {key} not submitted",form_name+"_messages")
	
	return valid
