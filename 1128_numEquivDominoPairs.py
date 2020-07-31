import collections    
def numEquivDominoPairs(dominoes):
	cnt = collections.Counter()
	res = 0
	for a, b in dominoes:
		## if tuple matches, then add 1
		res += cnt[(a, b)]
		## avoid count list like (1,1) twice
		if a != b:
			res += cnt[(b, a)]

		cnt[(a, b)] += 1

	return res 

if __name__ == '__main__':
	print(numEquivDominoPairs(dominoes = [[1,2],[2,1],[3,4],[5,6]]))
