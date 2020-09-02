from typing import List 

## brute force
def rangeSum(nums: List[int], n: int, left: int, right: int) -> int:
    res = []
    for i in range(len(nums)):
        prefix = 0
        for j in range(i, len(nums)):
            prefix += nums[j]
            res.append(prefix)
    
    res.sort()
    return sum(res[left-1:right]) % 1_000_000_007

## min heap O(N^2 logN) worst (but much faster on average) & O(N) space (32ms 100%)   
def rangeSum(nums: List[int], n: int, left: int, right: int) -> int:
    import heapq
    h = [(val, idx) for idx, val in enumerate(nums)]
    heapq.heapify(h)
    ans = 0
    ## index starting from 1
    for k in range(1, right+1):
        val, idx = heapq.heappop(h)
        ## start to add the element from left
        if k >= left: ans += val 

        ## if within the boundary, push into heap
        if idx + 1 > len(nums):
            heapq.heappush(h, (val + nums[idx+1], idx+1))

    return ans % 1_000_000_007
    

