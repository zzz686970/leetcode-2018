def sortedSquares(A: 'List[int]') -> 'List[int]':
	## O(nlogn)
	# ans = [el**2 for el in A]
	# ans.sort()
	# return ans

	## O(n)
	l, r = 0, len(A)-1
	ans = [0 for _ in range(len(A))]
	while l <= r:
		left, right = abs(A[l]), abs(A[r])
		if left > right:
			ans[r-l] = left ** 2
			l += 1
		else:
			ans[r-l] = right ** 2
			r -= 1

	return ans 


print(sortedSquares([-4,-1,0,3,10]))
