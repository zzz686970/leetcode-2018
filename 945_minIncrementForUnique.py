def minIncrementForUnique(A):
	cnt = need = 0
	for i in sorted(A):
		cnt += max(need-i, 0)
		need = max(need+1, i+1)
	
	return cnt 

print(minIncrementForUnique([1,2,2]))


