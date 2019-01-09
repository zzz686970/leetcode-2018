def solveNQueens(n):
	# ans = []
	# # dots = '.' * n
	# def dfs(queen, cur=0):
	# 	if cur==len(queen):
	# 		ans.append(queen[:])
	# 		# ans.append([dots[:el]+'Q'+dots[el+1:] for el in queen[:]])
	# 	else:
	# 		for col in range(n):
	# 			queen[cur] = col
	# 			for r in range(cur):
	# 				# flag = True
	# 				if queen[r]==col or r-queen[r]==cur-queen[cur] or r+queen[r]==cur+queen[cur]:#判断是否跟前面的皇后冲突
	# 					# flag = False
	# 					break
	# 			else:
	# 			# if flag:
	# 				dfs(queen, cur+1)
	# dfs([None]*n)
	# # return ans
	# # return [[dots[:idx] + 'Q' + dots[idx+1:] for idx in el] for el in ans]
	# return [ ["."*idx + "Q" + "."*(n-idx-1) for idx in el] for el in ans]

	## faster way
	ans = []
	def dfs(queen, xy_diff, xy_sum):
		cur = len(queen)
		if cur == n:
			ans.append(queen)
		for col in range(n):
			if col not in queen and cur-col not in xy_diff and cur+col not in xy_sum:
				dfs(queen+[col], xy_diff+[cur-col], xy_sum+[cur+col])

	dfs([],[],[])
	return [ ["."*idx + "Q" + "."*(n-idx-1) for idx in el] for el in ans]

	 
print(solveNQueens(4))

			