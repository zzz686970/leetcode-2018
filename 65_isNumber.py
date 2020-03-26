import string

def isNumber(s):
	invalid_list = list(filter(lambda x: x !='e', string.ascii_lowercase))
	if any(el in invalid_list for el in s):
		return False
	else:
		return True

print(isNumber(['fs 12']))