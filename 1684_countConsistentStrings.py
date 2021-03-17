class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
#         res = 0
#         for word in words:
#             if all(el in allowed for el in set(word)):
#                 res += 1
        
#         return res
    
        # return sum(all(c in allowed for c in w) for w in words)
    
        alphabet = sum(1 << ord(c) - ord('a') for c in allowed)
        return sum(all((alphabet & (1 << ord(c) - ord('a')) != 0 \
                        for c in word))  \
                        for word in words)