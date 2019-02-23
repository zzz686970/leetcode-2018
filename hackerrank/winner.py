#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'winner' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER_ARRAY andrea
#  2. INTEGER_ARRAY maria
#  3. STRING s
#

def winner(andrea, maria, s):
    # Write your code here
    andrea_score = 0
    maria_score = 0

    if s == 'Even':
        for a, b in zip(andrea[::2], maria[::2]):
            andrea_score += a-b
            maria_score +=  b - a 

    else:
        for a, b in zip(andrea[1::2], maria[1::2]):
            andrea_score += a-b
            maria_score +=  b - a 

    if andrea_score > maria_score:
        return 'Andrea'
    elif andrea_score < maria_score:
        return 'Maria'
    else:
        return 'Tie'

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     andrea_count = int(input().strip())

#     andrea = []

#     for _ in range(andrea_count):
#         andrea_item = int(input().strip())
#         andrea.append(andrea_item)

#     maria_count = int(input().strip())

#     maria = []

#     for _ in range(maria_count):
#         maria_item = int(input().strip())
#         maria.append(maria_item)

#     s = input()

#     result = winner(andrea, maria, s)

#     fptr.write(result + '\n')

#     fptr.close()
