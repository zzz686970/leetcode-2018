from typing import List
import bisect 

def triangleNumber(nums: List[int]) -> int:
    n = len(nums)
    nums.sort()
    ans = 0
    for i in range(len(nums)-1):
        for j in range(i+1, len(nums)):
            idx = bisect.bisect_left(nums, nums[i]+nums[j])
            if idx <= n and idx > j:
                ans += idx - j - 1
                
    
    return ans 


class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0
        n = len(nums)
        for i in range(2, n):
            l, r = 0, i-1
            while l < r:
                if nums[l] + nums[r] > nums[i]:
                    ans += r -l
                    r -= 1
                else:
                    l += 1
        
        return ans    

print(triangleNumber([2,2,3,4]))
print(triangleNumber([4,2,3,4]))
            