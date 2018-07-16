def longestCommonPrefix( strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    c = ""
    if len(strs) >= 1:
        for i in range(len(strs[0])):
            if all(strs[0][:i+1] in el[:i+1] for el in strs):
                c = strs[0][:i+1]
            else:
                return c            
    return c

a = ["flower","flow","flight"]
b = ["dog","racecar","car"]
print(longestCommonPrefix(b))
