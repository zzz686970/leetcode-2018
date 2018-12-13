def findErrorNums(nums):
	# import collections
	# arr = collections.Counter(nums)
	# ans = [[k-1, k, k+1] for k,v in arr.items() if v==2]
	# return  ans[0][:-1] if ans[-1] in nums else ans[0][1:]

	## way 2
	# l = len(nums)
	# alpha = -sum(nums) + l*(l+1) //2
	# beta = -sum(x*x for x in nums) + l*(l+1)*(2*l+1)//6

	# return [(beta-alpha)//2, (alpha+beta) //2]
	return [sum(nums) - sum(set(nums)), sum(range(1, len(nums)+1)) - sum(set(nums))]

print(findErrorNums([1,2,2,4]))