def reverseVowels(s):
	# vowels = {}
	# for index, char in enumerate(s):
	# 	if char.lower() in 'aeiou':
	# 		vowels[index] = char
	# newS = ""
	# for i in range(len(s)):
	# 	if i in vowels:
	# 		newS += vowels[i]
	# 	else:
	# 		newS += s[i]
	l, r = 0, len(s)-1
	list1 = [char for char in s]
	while l< r:
		if list1[l].lower() in 'aeiou':
			if list1[r].lower() in 'aeiou':
				list1[l], list1[r] = list1[r], list1[l]
				l, r  = l+1, r-1
			else:
				r = r-1
		else:
			l = l + 1
	return "".join(list1)

s = "leetcode"
print(reverseVowels(s))