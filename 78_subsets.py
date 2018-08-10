def subsets(nums):
	result = [[]]
	for el in sorted(nums):
		result += [item + [el] for item in result]

	return result
	# from itertools import chain
	# new_list = list(chain(el for el in nums))
	# return new_list

nums = ['a','b','c']
print(subsets(nums))