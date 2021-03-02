class Solution:
    def specialArray1(self, nums: List[int]) -> int:
        res = Counter(nums)
        i = max(nums)
        while i >= min(len(nums), min(nums)-1):
            if i == (sum([v for k,v in res.items() if k >= i])):
                return i
            i -= 1
        
        return -1
    def specialArray2(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        i = 0
        while i < len(nums) and nums[i] > i:
            i += 1
        
        return -1 if i < len(nums) and nums[i] == i else i
    
    def specialArray(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        left, right = 0, len(nums)
        while left < right:
            mid = left + (right - left) // 2
            if mid < nums[mid]:
                left = mid + 1
            else:
                right = mid
        
        return -1 if left < len(nums) and nums[left] == left else left