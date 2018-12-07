def countAndSay(n):
	## flatten
	# import itertools
	# def flatten(iterables):
	# 	for i in itertools.chain(iterables):
	# 		if hasattr(i, '__iter__'):
	# 			for j in flatten(i): yield j
	# 		else:
	# 			yield i

	## [y for x in list1 for y in x]
	s = "1"

	for i in range(1, n):
		result = [s[0]]
		values = [1]
		l = len(s)
		for j in range(1, l):
			if s[j] == result[-1]:
				values[-1] += 1
			else:
				result.append(s[j])
				values.append(1)

		s = ""
		for v, k in zip(values, result):
			s += str(v) + k
	return s

	# 	result.append((index, start))
	# 	return result
	# if n == 1:
	# 	return "1"
	# else:
	# 	list1 = currentCount(str(n))
	# return "".join([str(j[0]) +j[1]  for j in list1])

print(countAndSay(3))
