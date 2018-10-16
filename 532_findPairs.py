from collections import Counter
def findPairs(nums, k):
	## can't ac
	## time
	# ans = []
	# nums = sorted(nums)
	# for i in range(len(nums)):
	# 	if (nums[i]+k) in nums[i+1:]:
	# 		ans.append((nums[i], nums[i]+k))

	# print(ans)
	# return len(set(ans))

	result = Counter(nums)
	cnt = 0
	for el in result:
		if k > 0 and el+k in result or k==0 and result[el] > 1:
			cnt += 1
	return cnt


a = [1,3,1,5,4]
k = 0
print(findPairs(a, k))