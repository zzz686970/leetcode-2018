class Solution:
    def reformatNumber(self, number: str) -> str:
        numbers = number.replace('-', '').replace(' ','')
        res = ""
        for idx, el in enumerate(numbers[:((len(numbers) + 1) // 3 -1) * 3]):
            if res and (len(res) +1) % 4 == 0:
                res += '-'
            res += el
        
        leftover = numbers[((len(numbers) + 1) // 3 -1) * 3:]
        if len(leftover) == 4:
            res += '-' + leftover[:2] + '-' + leftover[2:] if res else leftover[:2] + '-' + leftover[2:]
        else:
            res += '-' + leftover if res else leftover
        
        return res