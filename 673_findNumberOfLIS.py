import collections
def findNumberOfLIS(nums):
	if not nums: return 0
	dp = [1 for _ in range(len(nums))]
	cnt = [1 for _ in range(len(nums))]
	res = maxL = 0

	for i in range(len(nums)):
		for j in range(i):
			if nums[i] > nums[j]:
				if dp[j] + 1 > dp[i]:
					dp[i] = dp[j] + 1
					cnt[i] = cnt[j]
				elif dp[j] + 1 == dp[i]:
					cnt[i] += cnt[j]

		if maxL < dp[i]:
			maxL = dp[i]
			res = cnt[i]
		elif maxL == dp[i]:
			res += cnt[i]

	return res 

print(findNumberOfLIS([1,3,5,4,7]))
print(findNumberOfLIS([1,3,6,5,4,7, 6, 1]))

print(findNumberOfLIS([2,2,2,2,2]))