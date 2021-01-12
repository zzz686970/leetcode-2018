class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        length = len(arr)
        res = 0
        for i, val in enumerate(arr, 1):
            res += (i * (length - i + 1) + 1) // 2 * val
        
        return res
    
        
            
            
            