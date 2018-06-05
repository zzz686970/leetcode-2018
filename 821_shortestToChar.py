def shortestToChar(S, C):
	index = []
	result = []
	start = 0

	while True:
		start = S.find(C, start)
		if start == -1:
			break

		index.append(start)
		start += 1

	for i in range(len(S)):
		if i not in index:

			result.append(min([i-j if i>j else j-i for j in index]))

		else:
			result.append(0)

	return result

S = "loveleetcode"
C = "e"
print(shortestToChar(S, C))