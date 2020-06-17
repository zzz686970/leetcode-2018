import collections
from typing import List 

def findLucky(arr):
	return max(k if k == v else -1 for k, v in collections.Counter(arr).items())

def findLucky(arr: List[int]) -> int:
    dic1 = collections.Counter(arr)
    ans = -1
    for el in set(arr):
        if el == dic1[el]:
            ans = max(ans, el)
    
    return ans 

if __name__ == '__main__':
	print(findLucky(arr = [2,2,3,4]))