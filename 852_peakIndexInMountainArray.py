def peakIndexInMountainArray(A):
	max_ele = max(A)
	return A.index(max_ele)


A = [0,2,1,0]

print(peakIndexInMountainArray(A))