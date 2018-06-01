import re
def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    stack = []
    for i in range(len(s)):
        if '[' == s[i] or '{' == s[i] or '{' == s[i]:
            stack.append(s[i])

        if ']' == s[i]:
            if stack == [] or stack.pop() !='[':
                return False
        if '}' == s[i]:
            if stack == [] or stack.pop() !='{':
                return False
        if ')' == s[i]:
            if stack == [] or stack.pop() !='(':
                return False

    if stack:
        return False

    else:
        return True

    # match = re.compile('\(.*\)|\[.*\]|\{.*\}')
    # result = re.findall(match, s)

print(isValid('()'))