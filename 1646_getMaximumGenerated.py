class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        # if n == 0: return 0
        # if n == 1: return 1
        # res = [0, 1]
        # for i in range(2, n+1):
        #     if i % 2 == 0:
        #         res.append(res[i//2])
        #     else:
        #         res.append(res[(i-1)//2] + res[(i-1)//2 + 1])
        # return max(res)
    
    
        nums = [0]*(n+2)
        nums[1] = 1
        for i in range(2, n+1):
            nums[i] = nums[i//2] + nums[(i//2)+1] * (i%2)
    
        return max(nums[:n+1])