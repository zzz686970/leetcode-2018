def findShortestSubArray(nums):
	from collections import Counter, defaultdict
	key_value = Counter(nums)
	size = len(nums)
	reversed_nums = nums[::-1]
	element = []
	degree = max(key_value.values())
	key = []
	for el, value in key_value.items():
		if value == degree:
			key.append(el)

	for x in key:
		element.append(size - 1 - reversed_nums.index(x) -  nums.index(x) + 1)


	return min(element)

nums = [1, 2, 2, 3, 1]
print(findShortestSubArray(nums))