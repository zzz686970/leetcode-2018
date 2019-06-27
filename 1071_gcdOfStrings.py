def gcdOfStrings(str1, str2):
	ans = ''
	a_str, b_str = sorted([str1, str2], key = len)
	for el in b_str:
		if el in a_str:
			ans += el
		else:

