class Solution:
    def convert(self, s: str, numRows: int) -> str:
        ## length is 1 or can't form zigzag
        if numRows == 1 or numRows >= len(s):
            return s
        
        ## each time we add one more step from the first row
        ## if we reach the bottom, we step back
        ## each char should be concated in the row it belongs to
        index, step = 0, 1
        res = [''] * numRows
        for c in s:
            res[index] += c
            if index == 0:
                step = 1
            elif index == numRows - 1:
                step = -1
            index += step
        
        return "".join(res)