def threeSumClosest(nums, target):
	nums.sort()
	result = nums[0] + nums[1] + nums[2]
	for i in range(len(nums) - 2):
		j, k = i + 1, len(nums) - 1
		while j < k:
			total_sum = nums[i] + nums[j] + nums[k]

			if total_sum == target:
				return total_sum 

			if abs(total_sum - target) < abs(result - target):
				result = total_sum 

			if total_sum < target:
				j += 1

			if total_sum > target:
				k -= 1

	return result 

if __name__ == '__main__':
	print(threeSumClosest(nums = [-1,2,1,-4], target = 1))