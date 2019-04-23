#!/bin/python3

import math
import os
import random
import re
import sys
import numpy as np 
from itertools import combinations

#
# Complete the 'resolvePrices' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER count
#  2. INTEGER total
#  3. STRING priceListStr
#

def split(a):
    if not a:
        return [[]]
    elif len(a) == 1:
        return [[a]]
    else:
        result = []
        for i in range(1, len(a) + 1):
            result += [(a[:i], *sub_split) for sub_split in split(a[i:])]
        return result

def resolvePrices(count, total, priceListStr):
	# Write your code here
	price_list = [el for el in priceListStr.split(',')]
	if not price_list or len(price_list) < count: return []
	## no help
	### if len(price_list) == count and sum(price_list) == total: return price_list
	result = split(price_list)
	for sub in result:
		if len(sub) == count:
			if total == sum([int("".join(el)) for el in sub]):
				return [int("".join(el)) for el in sub]

	return []

def resolvePrices2(count, total, priceListStr):
	price_list = priceListStr.split(',')
	result = []
	# for i in combinations(range(1, 4), 2):
	# 	print(i)
	for i in combinations(range(1, len(price_list)), count):
		print(np.split(price_list, i))
		result.append([int("".join(el)) for el in np.split(price_list, i)])
	

	ans = [el for el in result if sum(list(el)) == total]

	return ans[0] if ans else []


	

if __name__ == '__main__':
	# print(resolvePrices(2, 124245, '123,456,789'))
	print(resolvePrices2(2, 124245, '123,456,789'))

	# fptr = open(os.environ['OUTPUT_PATH'], 'w')

	# count = int(input().strip())

	# total = int(input().strip())

	# priceListStr = input()

	# result = resolvePrices(count, total, priceListStr)

	# fptr.write('\n'.join(map(str, result)))
	# fptr.write('\n')

	# fptr.close()
