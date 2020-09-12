def modifyString(s: str) -> str:
    s = list(s)
    for i, val in enumerate(s):
        need_to_fill = ['a','b','c']
        if val == '?':
            if i-1 >= 0 and s[i-1] in need_to_fill:
                need_to_fill.remove(s[i-1])
            if i + 1 < len(s) and s[i+1] in need_to_fill:
                need_to_fill.remove(s[i+1])
            s[i] = need_to_fill.pop(0)
    
    return "".join(s)