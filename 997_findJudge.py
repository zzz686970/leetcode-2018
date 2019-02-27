def findJudge(N, trust):
	## can't ac
	# import collections
	# result = collections.defaultdict(list)
	# trust_of_each = collections.defaultdict(list)
	# for el in trust:
	# 	result[el[1]].append(el[0])
	# 	trust_of_each[el[0]].append(el[1])
	# ans = [key for key,val in result.items() if len(val) == N-1 and key not in val]
	# return ans[0] if len(ans) and len(trust_of_each.get(ans[0], [])) == 0  else -1

	count = [0] * (N+1)
	for i, j in trust:
		count[i] -= 1
		count[j] += 1

	for i in range(1, N+1):
		if count[i] == N-1:
			return i 

	return -1

print(findJudge(2, [[1,2]]))
print(findJudge(3, [[1,3],[2,3],[3,1]]))

# assert 2 == findJudge(2, [[1,2]])
# assert 3 == findJudge(N = 3, trust = [[1,3],[2,3]])
# assert -1 == findJudge(N = 3, trust = [[1,2],[2,3]])
# assert 3 == findJudge(N = 4, trust = [[1,3],[1,4],[2,3],[2,4],[4,3]])