from flask import flash
import re

def validate(data,all_checks,form_name="form",strict=True,func=flash,result={}):
	data = dict(data)
	valid = True
	for key, key_checks in all_checks.items():
		result[key] = None
		if key in data:
			for check in key_checks:
				regex = re.compile(check["regex"])
				if regex.match(data[key]):
					result[key] = True
				else:
					valid = False
					result[key] = False

					func(check["error"],check["category"])
		elif strict and key not in data:
			valid = False

			func(f"Field {key} not submitted",form_name+"_messages")
	
	return valid
