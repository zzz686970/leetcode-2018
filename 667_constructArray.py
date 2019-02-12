# def constructArray(n, k):
# 	if k >= n : return []
# 	ans = [i+1 for i in range(n)]
# 	i = 1
# 	while i < k:
# 		ans = ans[:i] + ans[i:][::-1]

# 		i += 1

# 	return ans

def constructArray(n, k):
	## O(n) solution
	l, r = 1, k+1
	ans = []
	while l <= r:
		ans.append(l)
		l += 1
		if l <= r:
			ans.append(r)
			r -= 1

	for i in range(k+2, n+1):
		ans.append(i)

	return ans

print(constructArray(4, 2)) 




# [1,2,3,4,5]

# 1 --> 1,2,3,4,5
# 2 --> 1,5,4,3,2
# 3 --> 1,5,2,3,4
# 4 --> 1,5,2,4,3