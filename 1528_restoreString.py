def restoreString(s, indices):
	return "".join([el[0] for el in sorted(zip(s, indices), key = lambda x: x[1])])

def restoreString(s, indices):
	## O(n)
	res = [''] * len(s)
	for idx, val in enumerate(s):
		res[indices[idx]] = val 

	return "".join(res)

if __name__ == '__main__':
	print(restoreString(s = "abc", indices = [0,1,2]))
	print(restoreString(s = "codeleet", indices = [4,5,6,7,0,2,1,3]))
	print(restoreString(s = "aiohn", indices = [3,1,4,2,0]))
	print(restoreString(s = "aaiougrt", indices = [4,0,2,6,7,3,1,5]))
	print(restoreString(s = "art", indices = [1,0,2]))

