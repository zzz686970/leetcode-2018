class Solution:
    def sortSentence(self, s: str) -> str:
        return " ".join([el[:-1] for el in sorted(s.split(' '), key = lambda x: x[-1])])