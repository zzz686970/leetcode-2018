def smallerNumbersThanCurrent(nums):
	dic = {}
	for i, num in enumerate(sorted(nums)):
		if num not in dic:
			dic[num] = i 

	return [dic[num] for num in nums]

from bisect import bisect_left
from functools import partial
# class Solution:
#     def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
#         return [*map(sorted(nums).index, nums)]
    


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        return [*map(partial(bisect_left, sorted(nums)), nums)]
    
        # sorted_nums = sorted(nums)
        # return [bisect_left(sorted_nums, v) for v in nums]

if __name__ == '__main__':
	print(smallerNumbersThanCurrent([8,1,2,2,3]))