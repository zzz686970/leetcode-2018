def validateStackSequences(pushed, popped):
	"""
	:type pushed: List[int]
	:type popped: List[int]
	:rtype: bool
	"""
	res = []
	i = 0
	for x in pushed:
		res.append(x)
		while res and res[-1] == popped[i]:
			i += 1
			res.pop()

	return i == len(popped)

assert True == validateStackSequences(pushed = [1,2,3,4,5], popped = [4,5,3,2,1])
		