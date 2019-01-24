def sumSubseqWidths(A):
	# res = [[]]
	# for num in A:
	# 	res += [el + [num] for el in res]

	# return res 
	return sum(((1<<i) - (1<<(len(A)-i-1))) * num for i, num in enumerate(sorted(A)) ) % (10**9 + 7)

print(sumSubseqWidths(A=[2,1,3]))