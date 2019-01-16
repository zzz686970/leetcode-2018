def calcEquation(equations, values, queries):
	import itertools
	import collections
	res = collections.defaultdict(dict)
	final = []
	for (p1, p2), val in zip(equations, values):
		res[p1][p1] = res[p2][p2] = 1.
		res[p1][p2] = val 
		res[p2][p1] = 1/val 
	
	for k,i,j in itertools.permutations(res, 3):
		if k in res[i] and j in res[k]:
			res[i][j] = res[i][k] * res[k][j]

	return [res[p1].get(p2,-1.) for p1,p2 in queries]

	# for el in queries:
	# 	if el[0] in res and el[1] in res and res[el[0]][0] == res[el[1]][0]:
	# 		final.append(res[el[0]][1] / res[el[1]][1])
	# 	# elif el[0] in el[1]:
	# 	# 	final.append(1.)
	# 	else:
	# 		final.append(-1.)


# print(calcEquation(equations = [ ["a", "b"], ["b", "c"] ],
# values = [2.0, 3.0],
# queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ]))

print(calcEquation([["x1","x2"],["x2","x3"],["x3","x4"],["x4","x5"]],
[3.0,4.0,5.0,6.0],
[["x1","x5"],["x5","x2"],["x2","x4"],["x2","x2"],["x2","x9"],["x9","x9"]]))

[360.0,0.00833,20.0,1.0,-1.0,-1.0]