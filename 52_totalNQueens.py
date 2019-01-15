# def totalNQueens(n):
# 	cnt = 0
# 	def dfs(queen, cur=0):
# 		nonlocal cnt
# 		if cur == len(queen):
# 			cnt += 1
# 		else:
# 			for col in range(n):
# 				queen[cur] = col
# 				for r in range(cur):
# 					if queen[r] == col or  r - queen[r] == cur - queen[cur] or r+queen[r] == cur + queen[cur]:
# 						break
# 				else:
# 					dfs(queen, cur + 1)

# 	dfs([None]*n)

# 	return cnt 

# print(totalNQueens(4))

## way 2
def totalNQueens(n):
	ans = 0
	def dfs(queen, xy_diff, xy_sum):
		nonlocal ans
		cur = len(queen)
		if cur == n:
			ans += 1
		for col in range(n):
			if col not in queen and cur-col not in xy_diff and cur+col not in xy_sum:
				dfs(queen+[col], xy_diff+[cur-col], xy_sum+[cur+col])

	dfs([],[],[])
	return ans

print(totalNQueens(4))
