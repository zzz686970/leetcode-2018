class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        return sum(sorted(piles)[len(piles) // 3::2])
        # piles.sort()
        # res = 0
        # while piles:
        #     alice = piles.pop()
        #     res += piles.pop()
        #     piles.pop(0)

        # return res

        