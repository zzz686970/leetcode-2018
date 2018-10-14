import string
def reverseOnlyLetters(S):
	result=""
	sub = "".join([char for char in S if char in string.ascii_letters ])[::-1]
	cnt = 0
	for i in range(len(S)):
		if S[i] in string.ascii_letters:
			result += sub[cnt]
			cnt += 1
		else:
			# result += sub[::-1]
			# sub = ""
			result += S[i]
	# result += sub[::-1]


	return result

S = "a-bC-dEf-ghIj"
print(reverseOnlyLetters(S))