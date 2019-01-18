def numDistinct(s, t):
	import collections
	chars, index, dp = set(t), collections.defaultdict(list), [0]*len(t)

	for i, val in enumerate(t): index[val].append(i)
	print(index)
	for char in s:
		if char in chars:
			for i in index[char][::-1]:
				print(i)
			## if there are repeated chars 
				dp[i] += dp[i-1] if i >0 else 1
			print(dp)

	return dp[-1]

print(numDistinct(s = "rabbit", t = "rabbit"))