class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = []
        if not nums: return []
        for idx, num in enumerate(nums):
            if not res:
                res.append(str(num))
            if idx < len(nums) -1 and nums[idx+1] - num != 1:
                if res and res[-1] != str(num):
                    res[-1] += "->" + str(num)

                res.append(str(nums[idx+1]) )
            if idx + 1 == len(nums) -1 and res[-1] != str(nums[idx+1]):
                res[-1] += "->" + str(nums[idx+1])
        
        return res