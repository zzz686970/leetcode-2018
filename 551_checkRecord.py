def checkRecord(s):
	if s.count('A') <= 1 and 'LLL' not in s:
		return True

	return False

print(checkRecord('PPALLP'))
	# result = {}
	# for char in s:
	# 	result[char] = result[char] + 1 if char in result else 1

