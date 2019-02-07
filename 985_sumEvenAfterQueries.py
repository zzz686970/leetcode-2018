# def sumEvenAfterQueries(A, queries):
# 	## O(N^2)
# 	def find_even_sum(A):
# 		total = 0
# 		for i in A:
# 			if i % 2:
# 				continue
# 			else:
# 				total += i 
# 		return total 

# 	ans = []
# 	for query in queries:
# 		val, idx = query[0], query[1]
# 		A[idx] += val 
# 		ans += find_even_sum(A), 

# 	return ans 

# print(sumEvenAfterQueries(A = [1,2,3,4], queries = [[1,0],[-3,1],[-4,0],[2,3]]))

def sumEvenAfterQueries(A, queries):
	if not queries or not A: return []
	base = 0
	res = []
	for i in A:
		if i % 2 == 0:
			base += i 

	for query in queries:
		val, idx = query

		## A[idx] even val even
		if A[idx] % 2== 0 and val %2 == 0:
			base += val 

		## A[idx] odd val odd
		elif A[idx] % 2 and val % 2:
			base += A[idx] + val 

		## A[idx] even val odd 
		elif A[idx] % 2 ==0 and val % 2:
			base -= A[idx]

		A[idx] += val 

		res.append(base)

	return res 
