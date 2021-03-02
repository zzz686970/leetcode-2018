from statistics import mean  
class Solution:
    def trimMean(self, arr: List[int]) -> float:
    	## len(arr) // 20
    	## sum(sorted(arr)[n // 20 : -n // 20]) / (n * 9 // 10)
        l, r = int(len(arr) * 0.05), len(arr)-int(len(arr) * 0.05 )
        return mean(sorted(arr)[l:r])
