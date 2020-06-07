import collections
def canBeEqual(target, arr):
	return sorted(target) == sorted(arr)

	return collections.Counter(target) == collections.Counter(arr)