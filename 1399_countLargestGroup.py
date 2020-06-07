import collections
def countLargestGroup(n):
	groups = collections.Counter(map(lambda x: sum(map(int, str(x))) , range(1, n+1)))
	# group = groups.most_common()
	# sum(v == group[0][1] for k, v in group.items())
	mx = max(groups.values())
	return sum(v==mx for k,v in groups.items())