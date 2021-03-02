from itertools import count 
from operator import sub 

class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
#         ans = []
#         for i in range(len(s)):
#             for j in range(len(s)-1, 0, -1):
#                 if s[i] == s[j]:
#                     ans.append(j-i-1)
        
#         return max(ans) if ans else -1
        
#         max_len, indices = -1, {}
#         for idx, el in enumerate(s):
#             max_len = max(max_len, idx - indices.setdefault(el, idx+1))
        
#         return max_len

        print(list(map({}.setdefault, s, count(1))))
        print(list(map({}.setdefault, s, count())))
        ## 里面的map将s按照顺序排列，用setdefault检查key是否存在，如果不存在则从1开始计数，存在则用之前的数字
        ## 外面的map将得到的列表和count()进行相减，然后选取最大的长度
        return max(map(sub, count(), map({}.setdefault, s, count(1))))
        