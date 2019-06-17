#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'reassignedPriorities' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY issuePriorities as parameter.
#

def reassignedPriorities(issuePriorities):
	# Write your code here
	import collections
	pool = sorted(collections.Counter(issuePriorities).keys())
	new_order = {}
	ans = []
	for idx, key in enumerate(pool):
		new_order[key] = idx + 1
	for i in  issuePriorities:
		ans.append(new_order.get(i))
	return ans

if __name__ == '__main__':
	# fptr = open(os.environ['OUTPUT_PATH'], 'w')

	# issuePriorities_count = int(input().strip())

	issuePriorities = [1,4,4,8]
	reassignedPriorities(issuePriorities)
	# for _ in range(issuePriorities_count):
	#     issuePriorities_item = int(input().strip())
	#     issuePriorities.append(issuePriorities_item)

	# result = reassignedPriorities(issuePriorities)

	# fptr.write('\n'.join(map(str, result)))
	# fptr.write('\n')

	# fptr.close()
