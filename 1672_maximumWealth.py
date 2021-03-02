class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        # return max(sum(el) for el in accounts)
        return max(map(sum, accounts))