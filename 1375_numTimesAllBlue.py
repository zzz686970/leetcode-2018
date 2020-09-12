class Solution:
    def numTimesAllBlue(self, light: List[int]) -> int:
        res = right = 0
        for i, val in enumerate(light, 1):
            right = max(right, val)
            res += right == i
        
        return res

        # return sum(map(operator.eq, itertools.accumulate(A, max), itertools.count(1)))
        # return sum(i == m for i, m in enumerate(itertools.accumulate(A, max), 1))