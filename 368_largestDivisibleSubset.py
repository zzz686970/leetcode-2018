def largestDivisibleSubset(nums):
	dp = [[]]
	for n in sorted(nums):
		# print([n], "###", max((s for s in dp if not s or n % s[0]==0), key=len))
		## ensure the first element of each sub-list is the largest
		dp.append([n]+max((s for s in dp if not s or n % s[0]==0), key=len))
	return max(dp,key=len)

print(largestDivisibleSubset([1,2,4,8,10]))