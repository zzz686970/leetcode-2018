def customSortString(S, T):
	# result = {}
	index = []

	for char in S:
		start = 0

		while True:
			start = T.find(char, start)
			if start == -1:
				break

			index.append(start)
			start += 1
		# result[char] = index

	for i in range(len(T)):
		if i not in index:
			index.append(i)

	result = "".join([T[i] for i in index])


	return result


print(customSortString('cba', 'abcd'))


# def find_all(a_str, sub):
#     start = 0
#     while True:
#         start = a_str.find(sub, start)
#         if start == -1: return
#         yield start
#         start += len(sub) # use start += 1 to find overlapping matches

# list(find_all('spam spam spam spam', 'spam')) # [0, 5, 10, 15]

