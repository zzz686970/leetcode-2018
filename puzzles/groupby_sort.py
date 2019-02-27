import itertools
from itertools import groupby
from operator import itemgetter
import collections

a = [["d", 2], ["c", 5], ["a", 9], ["b", 4], ["b", 2], ["c", 9]]
res = collections.defaultdict(list)
x, y = zip(*a)
for i in range(len(x)):
	res[x[i]] += y[i],

print(sorted([(key, len(value), sum(value)/len(value)) for key, value in res.items()] , key = lambda x: (x[1]), reverse = True))

a = sorted(a, key=itemgetter(0))
lists = []

for key, group in groupby(a, itemgetter(0)):
    time_list = [item[1] for item in group]
    lists.append((key, len(time_list), sum(time_list) / len(time_list)))

print(sorted(lists, key=itemgetter(1), reverse=True))