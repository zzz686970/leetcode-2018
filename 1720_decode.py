class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        # ans = [first]
        # for el in encoded:
        #     ans.append(el ^ ans[-1])
        # return ans
        return list(accumulate([first] + encoded, lambda x, y: x ^ y))