def balancedStringSplit(s: str) -> int:
    i, l_cnt, r_cnt = 0, 0, 0 
    res = 0
    while i < len(s):
        if s[i] == 'L':
            l_cnt += 1
        else:
            r_cnt += 1
        i += 1
        if l_cnt != 0 and l_cnt == r_cnt:
            res += 1
            l_cnt, r_cnt = 0, 0 

    return res 

from itertools import accumulate
def balancedStringSplit(s: str) -> int:
    ## a space before L
    return list(acc(map(' L'.find, s))).count(0)
    return list(acc(map({'L':1,'R':-1}.get, s))).count(0)
    return list(acc(1 if c == 'L' else -1 for c in s)).count(0)

def balancedStringSplit(s: str) -> int:
    res = cnt = 0
    for c in s:
        cnt += c == 'L'
        cnt -= c == 'R'
        res += cnt == 0
    return res 



print(balancedStringSplit("RLRRLLRLRL"))
print(balancedStringSplit("RLLLLRRRLR"))
print(balancedStringSplit("LLLLRRRR"))
print(balancedStringSplit("RLRRRLLRLL"))
