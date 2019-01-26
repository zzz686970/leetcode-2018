def arrayNesting(nums):
	visited, res = [0] * len(nums), 0
	for num in nums:
		cnt, j = 0, num
		while not visited[j]:
			visited[j], cnt, j = 1, cnt+1, nums[j]

		res = max(res, cnt)
	
	return res

