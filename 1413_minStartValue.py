def minStartValue(nums):
	start_val, total_sum = 1, 0
	for i in nums:
		total_sum += i 
		while start_val + total_sum < 1:
			start_val += 1


	return start_val

import itertools
def minStartValue(nums):
	# return max(1, max(1 - prefix_sum for prefix_sum in itertools.accumulate(nums)))
	start_val, total_sum = 1, 0
	for i in nums:
		total_sum += i 
		start_val = max(start_val, 1 - total_sum)


	return start_val	

if __name__ == '__main__':
	print(minStartValue(nums = [-3,2,-3,4,2]))