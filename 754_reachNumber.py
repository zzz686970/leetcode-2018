class Solution():
	def reachNumber(self, target):
		result = 0
		for i in range(888888):
			result += i 
			if abs(target) <= abs(result) and target % 2 == result % 2:
				return i 



