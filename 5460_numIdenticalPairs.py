from typing import List 
import collections 

def numIdenticalPairs(nums: List[int]) -> int:
    res = collections.Counter(nums)
    return sum(map(lambda x: (x-1)*x // 2, res.values()))

if __name__ == '__main__':
	print(numIdenticalPairs(nums = [1,2,3,1,1,3]))
	print(numIdenticalPairs(nums = [1,1,1,1]))
	print(numIdenticalPairs(nums = [1,2,3]))