def longestPalindrome(s):
	from collections import Counter
	ans = 0
	for k, count in Counter(s).items():
		ans += count // 2

	## check whether it's odd or not
	return ans*2 + (len(s) > ans*2)


print(longestPalindrome('abc'))