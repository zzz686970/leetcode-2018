def longestPalindrome(s):
	if len(s) == 0: return ''
	## one number is always a palindrome
	start, length = 0, 1
	for i in range(len(s)):
		## ofo
		if i-length >= 1 and s[i-length-1:i+1] == s[i-length-1:i+1][::-1]:
			start = i-length-1
			length += 2
		
		## ooo
		if i - length>=0 and s[i-length:i+1] == s[i-length:i+1][::-1]:
			start = i-length
			length += 1

	return s[start:start+length]

print(longestPalindrome('abcdedc'))