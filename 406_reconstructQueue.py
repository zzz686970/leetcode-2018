def reconstructQueue(people):
	## O(n^2)
	# res = []
	# people = sorted(people, key = lambda x: (-x[0],x[1]))
	# print(list(people))
	# for p in people:
	# 	res.insert(p[1],p)
	# 	# print(res)

	# return res 

	## O(nlogn)
	blocks = [[]]

	for p in sorted(people, key=lambda pair: (-pair[0], pair[1])):
		index = p[1]
		for i, block in enumerate(blocks):
			m = len(block)
			if index <= m:
				break 
			index -= m 

		block.insert(index, p)
		if m * m > len(people):
			print(m, i, p,  block,'####', blocks)

			blocks.insert(i+1, block[m//2:])
			print(m, i, p,  block,'--->', blocks)
			del block[m//2:]
			print(m, i, p,  block,'&&&&&', blocks)

	return [p for block in blocks for p in block]


	## O(n sqrt(n))
	


print(reconstructQueue([[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]))