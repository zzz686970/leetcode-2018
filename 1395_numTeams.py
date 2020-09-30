class Solution:
    def numTeams1(self, rating: List[int]) -> int:
        if len(rating) <= 2: 
            return 0
        n = len(rating)
        cnt = 0
        for i in range(n-2):
            for j in range(i+1, n-1):
                for k in range(j+1, n):
                    if rating[i] < rating[j] < rating[k] or rating[i] > rating[j] > rating[k]:
                        cnt += 1
        
        return cnt
    
    def numTeams(self, rating: List[int]) -> int:
        if len(rating) <= 2:
            return 0
        cnt = 0
        for i, v in enumerate(rating):
            left_cnt = [0, 0]
            right_cnt = [0, 0]
            for v1 in rating[:i]:
                if v1 > v:
                    left_cnt[1] += 1
                if v1 < v:
                    left_cnt[0] += 1
            
            for v2 in rating[i+1:]:
                if v2 > v:
                    right_cnt[1] += 1
                if v2 < v:
                    right_cnt[0] += 1
            
            cnt += left_cnt[0] * right_cnt[1] + left_cnt[1] * right_cnt[0]
        
        return cnt