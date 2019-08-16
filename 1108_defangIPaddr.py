def defangIPaddr(address):
	res = ''
	for el in address:
		if el == '.':
			res += '[.]'
		else:
			res += el

	# return res

	## one line
	return "[.]".join(address.split('.'))

print(defangIPaddr("1.1.1.1"))
