def gcdOfStrings(str1, str2):
	if len(str1) == len(str2):
		return str1 if str1 == str2 else ''
	a_str, b_str = sorted([str1, str2], key = len)
	if b_str[:len(a_str)] == a_str:
		return gcdOfStrings(b_str[len(a_str):], a_str)
	else:
		return ''

print(gcdOfStrings(str1 = "ABABAB", str2 = "ABAB"))

