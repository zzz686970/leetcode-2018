class Solution:
    def minSteps(self, s: str, t: str) -> int:
        res = collections.Counter(s) - collections.Counter(t)
        return sum(res.values())