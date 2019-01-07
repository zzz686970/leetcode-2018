def subsets(nums):
	# result = [[]]
	# for el in sorted(nums):
	# 	result += [item + [el] for item in result if item+[el] not in result]

	# return [i for i in result]

	## faster way2
	# import collections
	# res = [[]]
	# for num, freq in collections.Counter(nums).items():
	# 	l = len(res)
	# 	for i in range(1, freq+ 1):
	# 		for r in res[:l]:
	# 			res.append(r+[num]*i)
	# return res

	## way 3
	result = [[]]
	for el in sorted(nums):
		result += [item + [el] for item in result]
	dic = {}
	for i in result:
		dic[str(i)] = 0

	return [eval(key) for key in dic.keys()]



	# from itertools import chain
	# new_list = list(chain(el for el in nums))
	# return new_list

import random
nums = []
for i in range(10):
	nums.append(random.randint(1,5))
print(nums)
print(subsets(nums))