def toGoatLatin(S):
	vowel = ['a','e','i','o','u']
	list1 = S.split(" ")
	result = []
	for ele in list1:
		if ele[:1].lower() in vowel:
			result.append(ele+"ma")
		else:
			result.append(ele[1:]+ele[0:1]+'ma')
	result1 = [ele+(index+1)*'a' for index, ele in enumerate(result)]
	return " ".join(result1)

S = "I speak Goat Latin"
print(toGoatLatin(S))
