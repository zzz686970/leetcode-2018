def minDeletionSize(A):
	cnt = 0
	for num in zip(*A):
		if list(num) != list(sorted(num)):
			cnt += 1
	return cnt
print(minDeletionSize(A=['cba','daf','ghi']))