def findDisappearedNumbers(nums):
	max_number = max(nums)
	min_number = min(nums)
	ans = []
	for i in range(min_number, max_number+1):
		if i not in nums:
			ans.append(i)

	return ans

nums = [4,3,2,7,8,2,3,1]
print(findDisappearedNumbers(nums))