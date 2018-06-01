def numJewelsInStones(J, S):
	"""
	:type J: str
	:type S: str
	:rtype: int
	""" 
	result = 0
	for char in J:
		result += S.count(char)

	return result

J = 'aA'
S = 'aAAA'

print(numJewelsInStones(J, S))