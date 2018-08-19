def uncommonFromSentences(A, B):
	list2 = A.split(" ") + B.split(" ")
	result = dict()
	ans = []
	for ele in list2:
		if ele in result:
			result[ele] += 1
		else:
			result[ele] = 1

	for key, value in result.items():
		if value == 1:
			ans.append(key)

	return ans

A = "this apple is sweet"
B = "this apple is sour"

print(uncommonFromSentences(A, B))