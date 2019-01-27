def compareVersion(version1, version2):
	import itertools
	for a, b in itertools.zip_longest(version1.split('.'), version2.split('.'), fillvalue=0):
		if int(a) > int(b):
			return 1
		elif int(a) < int(b):
			return -1

	return 0

	## optimize
	# v1, v2 = map(int, v1.split('.')), map(int, v2.split('.'))
	# v1, v2 = zip(*itertools.zip_longest(v1, v2, fillvalue=0))
	# return (0, 1, -1)[(v1>v2)-(v1<v2)]

	## recursive
	main1, _, rest1 = ('0' + version1).partition('.')
	main1, _, rest1 = ('0' + version2).partition('.')
	return cmp(int(main1), int(main2)) or len(rest1+rest2) and self.compareVersion(rest1, rest2)

# print(compareVersion(version1 = "0.1", version2 = "1.1"))
# print(compareVersion(version1 = "7.5.2.4", version2 = "7.5.3"))
# print(compareVersion(version1 = "1.01", version2 = "1.001"))

print(compareVersion(version1 = "1.0", version2 = "1.0.0"))