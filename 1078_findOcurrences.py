def findOcurrences(text, first, second):
	if len(text) <= 2: return []
	arr = text.split(' ')
	ans = []
	for i in range(len(arr)-2):
		if arr[i] == first and arr[i+1] == second:
			ans.append(arr[i+2])

	return ans

	## way 2
	# positive lookahead  match a single character not present in the list below
	# return re.findall(first + " " + second + ' (?=[^\s]+)', text)


# findOcurrences(text = "alice is a good girl she is a good student", first = "a", second = "good")
findOcurrences("jkypmsxd jkypmsxd kcyxdfnoa jkypmsxd kcyxdfnoa jkypmsxd kcyxdfnoa kcyxdfnoa jkypmsxd kcyxdfnoa",
               	"kcyxdfnoa",
               	"jkypmsxd")