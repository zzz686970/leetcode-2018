import string
print(string.ascii_uppercase)
def convertToTitle(n):
	return "" if n == 0 else convertToTitle(int((n - 1) / 26)) + chr((n - 1) % 26 + ord('A'))

	# index = dict()
	# for i in range(1, 27):
	# 	index[i] = string.ascii_uppercase[i-1]
	# ans = ""
	# while True:
	# 	if n > 26:
	# 		ans += index.get(int((n-1)/26), 'A')
	# 		n = n%26
	# 	else:
	# 		ans += index.get(int(n%26), 'Z')
	# 		break
	# return ans

n= 10
print(convertToTitle(703))