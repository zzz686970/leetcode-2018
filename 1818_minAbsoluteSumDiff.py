from typing import List 

class Solution:
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        arr = sorted(nums1)
        total, ans = 0, inf 
        for i in range(len(nums1)):
            ## difference of two elements
            diff = abs(nums1[i] - nums2[i])
            total += diff 
            idx = bisect.bisect_left(arr, nums2[i])
            ## compare with left element
            if idx:
                ans = min(ans, abs(arr[idx-1]- nums2[i]) - diff)
            ## compare with the right element
            if idx < len(nums2):
                ans = min(ans, abs(arr[idx] - nums2[i]) - diff)

        ## if total == 0, return directly
        ## if total != 0 subtract ans 
        return (total + ans) % (10 ** 9 + 7) if total else total 
                

print(minAbsoluteSumDiff([1,28,21],[9,21,20]))