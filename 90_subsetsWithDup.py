class Solution:
	def subsetsWithDup(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[List[int]]
		"""
		import collections

		result = [[]]
		## generate dict with {num: freq}
		## get the currrent length of result
		## iteration: num should be iterated freq times
		## use the current lenght of result to append new value
		for num, freq in collections.Counter(nums).items():
			l = len(result)
			for i in range(1, freq+1):
				for el in result[:l]:
					result.append(el + [num] * i)

		return result 
		
		# result = [[]]
		# for el in sorted(nums):
		# 	result += [item + [el] for item in result if item+[el] not in result]

		# return [i for i in result]