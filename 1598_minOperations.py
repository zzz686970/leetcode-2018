class Solution:
    def minOperations(self, logs: List[str]) -> int:
        ans = 0
        for log in logs:
            if log == '../':
                ans = max(0, ans-1)
            elif log.endswith('/') and log[-2] !='.':
                ans +=1 
        
        return ans
    
        return reduce(lambda depth, folder: max(0, depth - folder.rfind('.')), logs, 0)