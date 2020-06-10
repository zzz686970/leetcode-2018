import collections
from typing import List 

def uniqueOccurrences(arr: List[int]) -> bool:
    res = collections.Counter(arr).values()
    return len(set(res)) == len(res)

def uniqueOccurrences(arr: List[int]) -> bool:
	"""[summary]
	
	bucket 1~1000
	
	Arguments:
		arr {List[int]} -- [description]
	
	Returns:
		bool -- [description]
	"""
	total = [0] * 2001
	for i in arr: total[i+1000] += 1

	bucket = [0] * 1000
	for i in total:
		if i:
			bucket[i-1] += 1
			if bucket[i-1] > 1: 
				return False

	return True


if __name__ == '__main__':
	print(uniqueOccurrences(arr = [1,2,2,1,1,3]))
	print(uniqueOccurrences(arr = [1,2]))
	print(uniqueOccurrences(arr = [-3,0,1,-3,1,1,1,-3,10,0]))
