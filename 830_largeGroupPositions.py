import re
class Solution:
	def largeGroupPositions(self, S):
		"""
		:type S: str
		:rtype: List[List[int]]
		"""
		# low, high = 0, 0
		# result = []
		# while high < len(S) :
		# 	if low == high: high += 1
		# 	if high < len(S) and S[low] == S[high]:
		# 		high += 1
		# 	else:
		# 		if high - low > 2:
		# 			result.append([low, high-1])
		## 		if high - low == 2 and S[high] == S[low]:
		## 			result.append([low, high])
		# 		low = high
		# if high -low > 2:
		# 	result.append([low, high-1])
		# return result

		## way 2
		# low = 0
		# ans = []
		# while low < len(S):
		# 	high = low + 1
		# 	while high < len(S) and S[low] == S[high]:
		# 		high += 1
		# 	if (high - low) > 2:
		# 		ans.append([low, high-1])
		# 	low = high

		return [[r.start(),r.end()-1] for r in re.finditer(r'(\w)\1{2,}', S)]

a = Solution()
print(a.largeGroupPositions('aaa'))
