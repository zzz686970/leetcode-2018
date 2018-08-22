def repeatedStringMatch(A, B):
	start = int(len(B) / len(A))
	# for i in range(len(B)-2):
	# 	if B[i:i+2] not in A*2:
	# 		return -1
	for i in range(start, start+3):
		if len(A*i) > len(B) and  B in A*i:
			return i
	return -1

A = "baaaabbbba"
B = "bbaaaabbbbaabaaaabbbbaabaaaabbbbaabaaaabbbbaabaaaabbbbabbaaaabbbbabbaaaabbbbabbaaaabbbbabbaaaabbbbaa"
print(repeatedStringMatch(A, B))