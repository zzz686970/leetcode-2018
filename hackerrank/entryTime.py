#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'entryTime' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. STRING keypad
#

def entryTime(s, keypad):
    if not s: return 0
    # Write your code here
    # nums = list(map(lambda x: keypad[3*x:(x+1)*3], range(3)))
    result = {}
    ans = 0
    n = len(keypad)
    for i, val in enumerate(keypad):
        result[val] = [i//3, i%3]
    directions = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
    for i in range(1, len(s)):
        prev = result.get(s[i-1])
        tmp = [[x+y for x, y in zip(direction,prev)] for direction in directions]
        if s[i] != s[i-1] and (result[s[i]] in tmp):
            ans += 1
        elif s[i] == s[i-1]:
            ans += 0
        else:
            ans += 2
    return ans




if __name__ == '__main__':
    print(entryTime('91566165', '639485712'))
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # s = input()

    # keypad = input()

    # result = entryTime(s, keypad)

    # fptr.write(str(result) + '\n')

    # fptr.close()
