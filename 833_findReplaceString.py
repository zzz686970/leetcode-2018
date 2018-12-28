def findReplaceString(S, indexes, sources, targets):
	"""
	:type S: str
	:type indexes: List[int]
	:type sources: List[str]
	:type targets: List[str]
	:rtype: str
	"""
	## way1
	# ans = [ch for ch in S]
	# bias = 0
	# for idx, s, t in sorted(zip(indexes, sources, targets)):
	# 	if S[idx:idx+len(s)] == s:
	# 		ans = ans[:idx+bias] + [t] + ans[idx+bias+len(s):]
	# 		bias += 1 - len(s)

	# return "".join(ans)

	## way 2
	for i, s, t in sorted(zip(indexes, sources, targets), reverse=True):
		S = S[:i] + t + S[i+len(s):] if S[i:i+len(s)] == s else S

	return S

	# indexes, sources, targets = zip(*tuple(sorted(zip(indexes, sources, targets))))
	# print(indexes, sources, targets)
	# ans = ''
	# while j < len(indexes):
	# 	if S[]
	# res = ''
	# i, j = 0, 0
	# # while j < len(indexes):
	# while i < len(S) and j < len(indexes):
	# 	# print('i:{},j:{}'.format(i,j))
	# 	if i < indexes[j]:
	# 		res += S[i]
	# 	elif i == indexes[j]:
	# 		if sources[j] == S[i:i+len(sources[j])]:
	# 			res += targets[j]
	# 			i += len(sources[j])
	# 			j += 1
	# 			break
	# 		else:
	# 			res += S[i]
	# 	else:
	# 		j += 1
	# 	i += 1
	# 	# j += 1
	# if i < len(S):
	# 	res += S[i:]

	# return res


# print(findReplaceString(S = "abcd", indexes = [0,2], sources = ["a","cd"], targets = ["eee","ffff"]))
print(findReplaceString(S = "abcd", indexes = [0,2], sources = ["ab","ec"], targets = ["eee","ffff"]))
# print(findReplaceString("vmokgggqzp",[3,5,1],["kg","ggq","mo"], ["s","so","bfr"]))

# print(findReplaceString("mhnbzxkwzxtaanmhtoirxheyanoplbvjrovzudznmetkkxrdmr",[46,29,2,44,31,26,42,9,38,23,36,12,16,7,33,18],["rym","kv","nbzxu","vx","js","tp","tc","jta","zqm","ya","uz","avm","tz","wn","yv","ird"],["gfhc","uq","dntkw","wql","s","dmp","jqi","fp","hs","aqz","ix","jag","n","l","y","zww"]))
# "vbfrssozp"
# vmossozp


# "mhnbzxkwzxtaanmhtoirxheyanoplbvjrovzudznmetkkxrdmr"
# "mhnbzxkwzxtaanmhtoirxheaqznoplbvjrovzudznmetkkxrdmr"
# mhnzxkwxaamhtixheaqznoplbvjrovzudznmetkkxrdmr




