def numRabbits(answers):
	res = {}
	## how many groups we need for x+1 rabbits?
	## i + c[i] for those who claim having the same color
	## // (i+1) for groups
	import collections
	ans = collections.Counter(answers)
	res = 0
	for i in ans:
		res += (ans[i]+i) //(i+1)  * (i+1)

	return res

	## one line
	# ans = collections.Counter(answer)
	# return sum((ans[i]+i)//(i+1) * (i+1) for i in ans)

print(numRabbits(answers = [1, 1, 2]))