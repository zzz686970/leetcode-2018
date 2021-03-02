class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        new_word = word
        res = 0
        while new_word in sequence:
            new_word += word
            res += 1
        
        return res