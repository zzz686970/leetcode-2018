def reverseStr(s, k):
	list1 = [char for char in s]
	l = len(s)
	first = int(l / (2*k))
	second = l % (2 * k)
	if first:
		for i in range(first * 2 * k):
			if (i+1) % (2*k) == k and 2 * k <= l:
				list1[i+1-k:i+1] = list1[i+1-k:i+1][::-1]
	if second:
		if second <= k:
			list1[first * 2 * k:] = list1[first*2*k:][::-1]
		else:
			list1[first*2*k: first*2*k+k] = list1[first*2*k: first*2*k+k][::-1]

	print(list1)
	return "".join(list1)

s = "abcd"
k = 4
print(reverseStr(s, k))