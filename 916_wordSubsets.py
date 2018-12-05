def wordSubset(A, B):
	ans = []
	chk = {}
	from collections import Counter
	for sub in B:
		for el in sub:
			cnt = sub.count(el)
			if el not in chk or cnt > chk[el]:
				chk[el] = cnt

	# for s in A:
	# 	result = Counter(s)
	# 	# for el in set(B):
	# 	if all(s.count(el) >= 1 and s.count(el) >= chk[el] for el in set("".join(B))):
	# 		ans.append(s)
	s = set(A)
	for ele in A:
		for ch in chk:
			if ele.count(ch) < chk[ch]:
				s.remove(ele)
				break



	return list(s)

A = ["amazon","apple","facebook","google","leetcode"]
B = ["e","o"]
print(wordSubset(A, B))