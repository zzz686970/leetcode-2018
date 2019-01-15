def frequencySort(s):
	import collections
	return "".join(el[0]*el[1] for el in collections.Counter(s).most_common())

print(frequencySort('tree'))