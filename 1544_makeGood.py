def makeGood(s: str) -> str:
    res = ''
    i = 0
    while i < len(s) :
        if i < len(s)-1 and abs(ord(s[i]) - ord(s[i+1])) == 32:
            i += 2
            continue
        if res and abs(ord(res[-1]) - ord(s[i])) == 32:
            res = res[:-1]
            i += 1
            continue
        res += s[i]
        i += 1
            
    return res