def numSpecialEquivGroups(A):
	sub = dict()
	groups = [A[0]]
	for el in A:
		if len(el) >=2:
			key = (tuple(sorted(el[::2])), tuple(sorted(el[1::2])))
			sub[key] = sub.get(key, 0) + 1
		else:
			sub[el]= sub.get(el, 0) + 1

	return len(sub)



a = ['abcd','acbd','cbad']
print(numSpecialEquivGroups(a))

		# even = 
		# if i in range(len(el)):

		# potential = 
		# sub.append(el)
