import string
def isPalindrome(s):
	list1 = [char.lower() for char in s if char in string.ascii_letters + string.digits]
	if "".join(list1) == "".join(list(reversed(list1))):
		return True
	return False

print(isPalindrome("0P"))