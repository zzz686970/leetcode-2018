def isPalindrome( x):
	c = "".join(char for char in reversed(str(x)))
	return True if str(x) == c else False

isPalindrome(121)