import collections
from collections import OrderedDict
def largestValsFromLabels(values, labels, num_wanted, use_limit):
	arr = collections.defaultdict(list)
	for (x, y)  in zip(values, labels):
		arr[x].append(y)
	arr = sorted(arr.values(), key=lambda t: t, reverse = True)
	print(arr)


	return arr 
	# idx, cnt, used, res = 0, 0, 0, 0
	# while used < num_wanted:

largestValsFromLabels(values = [1,8,8,7,6], labels = [0,3,4,1,1], num_wanted = 3, use_limit = 1)