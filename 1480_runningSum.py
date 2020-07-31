def runningSum(nums):
	return [sum(nums[:i+1]) for i in range(len(nums)) ] 


from itertools import accumulate

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        # return [sum(nums[:i+1]) for i in range(len(nums)) ]
        return accumulate(nums)
        	