def findSubsequences(nums):
	import collections 
	# nums.sort()
	# result = [[]]
	# for num, freq in collections.Counter(nums).items():
	# 		l = len(result)
	# 		for i in range(1, freq+1):
	# 			for el in result[:l]:
	# 				result.append(el + [num] * i)
	subs = {()}
	for num in nums:
		tmp = {()}
		tmp |= {(num,)}
		for sub in subs:
			if sub and sub[-1] <=num:
				tmp |= {sub +(num,)}
		subs |= tmp 

		# subs |= {sub + (num,) for sub in subs if not sub or sub[-1] <= num}

	return [list(el) for el in  subs if len(el)>=2]


print(findSubsequences([1,2,3,4]))