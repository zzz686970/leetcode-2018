class Solution(object):
	def matrixScore(self, A):
		"""
		:type A: List[List[int]]
		:rtype: int
		"""
		m,n = len(A),len(A[0])
		# 行变换
		for i in range(m):
			if A[i][0] == 1: continue
			for j in range(n):
				A[i][j] = 1 - A[i][j]

		# 列变换
		res = 0
		for rows in zip(*A):
			# 始终使1的个数是更大的
			cnt1 = max(rows.count(1), rows.count(0))
			res += cnt1 * 2**(n-1)
			n -= 1
		return res