def buildArray(target, n):
	ans = []
	mapping = set(target)
	for i in range(1, n+1):
		ans.append('Push')
		if i not in mapping:
			ans.append('Pop')
		if i == target[-1]:
			break

	return ans 

if __name__ == '__main__':
	print(buildArray(target = [1,3], n = 3))
	print(buildArray([1,2], 4))
	print(buildArray([1,2], 9))
	print(buildArray(target = [2,3,4], n = 4))
