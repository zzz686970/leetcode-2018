def hIndex(citations) -> int:
	if not citations: return 0
	n = len(citations)
	l, r = 0, n - 1
	while l < r:
		mid = (l + r) // 2
		if citations[mid] == n - mid:
			return n
		elif citations[mid] < n - mid: 
			l = mid + 1
		else:
			r = mid 

	return min(citations[l], n - l )

print(hIndex([0,1,3,5,9]))
print(hIndex([1]))


def hIndex(citations) -> int:
	n = len(citations)
	l, r = 0, n - 1
	while l <= r:
		mid = (l + r) // 2
		if citations[mid] < n - mid: 
			l = mid + 1
		else:
			r = mid - 1 

	return n - l

print(hIndex([0,1,3,5,9]))
print(hIndex([1]))

def hIndex(citations) -> int:
	n = len(citations)
	if n == 0: return 0
	while l < r:
		mid = (l + r) // 2
		if citations[mid] < n - mid:
			l = mid + 1
		else:
			r = mid 

	return 0 if citations[l] + l < n else n - l