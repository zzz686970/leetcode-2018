import math
def maxProduct(nums):
    ans = list(sorted(nums))

    return (ans[-1]-1) * (ans[-2] - 1)

def maxProduct(nums):
    ## O(N) method
    m = n = -math.inf
    for num in nums:
        if num >= m:
            n = m 
            m = num 
        elif num > n:
            n = num 

    return (m-1) * (n-1)