def validPalindrome(s):
	## can't ac
	# list1 = [char for char in s]
	# l, r = 0, len(s)-1
	# if s == "".join(list(reversed(s))):
	# 	return True
	# else:
	# 	for i in range(len(list1)):
	# 		new_list = list1[0:i]+list1[i+1:len(s)]
	# 		if "".join(new_list) == "".join(list(reversed(new_list))):
	# 			return True

	# return False

	isPalindrome = lambda s: s == s[::-1]
	strPart = lambda s, x: s[:x]+s[x+1:]
	l, r = 0, len(s)-1
	while l < r:
		if s[l] != s[r]:
			return isPalindrome(strPart(s, l)) or isPalindrome(strPart(s, r))

		l, r = l+1, r-1

	return True


print(validPalindrome("abc"))