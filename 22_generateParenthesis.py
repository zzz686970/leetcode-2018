class Solution:
	def generateParenthesis(self, n):
		result = []
		self.generateParenthesisRecu(result, "", n, n)
		return result

	def generateParenthesisRecu(self, result, current, left, right):
		if left == 0 and right == 0:
			result.append(current)
		if left > 0:
			self.generateParenthesisRecu(result, current+"(", left-1, right)
		if left < right:
			self.generateParenthesisRecu(result, current+")", left, right-1)

if __name__ == '__main__':
	print(Solution().generateParenthesis(3))