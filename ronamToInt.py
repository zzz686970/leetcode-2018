def romanToInt(s):
	"""
	:type s: str
	:rtype: int
	"""
	a = 0
	for char in s:
		if 'I' in char:
			a += 1
		elif 'V' in char:
			a += 5
		elif 'X' in char:
			a += 10
		elif 'L' in char:
			a += 50
		elif 'C' in char:
			a += 100
		elif 'D' in char:
			a += 500
		elif 'M' in char:
			a += 1000

	if 'IV' in s or 'IX' in s:
		a -= 2
	if 'XL' in s  or 'XC' in s:
		a -= 20
	if 'CD' in s or 'CM' in s:
		a -= 200

	return a


	# for char in s:
	# 	if  char == 'I':
	# 		a += 1
	# 	elif char == 'V':
	# 		a += 5
	# 	elif char == 'X':
	# 		a += 10
	# 	elif char =='L':
	# 		a += 50
	# 	elif char =='C':
	# 		a += 100
	# 	elif char == 'D':
	# 		a += 500
	# 	elif char == 'M':
	# 		a += 1000

	# return a

print(romanToInt("MCMXCIV"))


