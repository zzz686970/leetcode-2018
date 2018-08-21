def strStr(haystack, needle):
	if needle == "":
		return 0
	elif haystack.find(needle) != -1:
		return haystack.index(needle)

	return -1

haystack = "aaaaa" 
needle = "bba"
print(strStr(haystack, needle))