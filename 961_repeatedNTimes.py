def repeatedNTimes(A):
	return (sum(A)-sum(set(A))) // (len(A)//2-1)