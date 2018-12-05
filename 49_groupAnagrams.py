# def in_nested_list(my_list, item):
# 	"""
# 	Determines if an item is in my_list, even if nested in a lower-level list.
# 	"""
# 	if item in my_list:
# 		return True
# 	else:
# 		return any(in_nested_list(sublist, item) for sublist in my_list if isinstance(sublist, list))

import collections
def groupAnagrams(strs):
	## can't ac
	# result = []
	# from itertools import permutations
	# for s in strs:
	# 	if result:
	# 		if any(s in sl for sl in result):
	# 		# if in_nested_list(result, s):
	# 			# ans[ans]
	# 			pass
	# 		else:
	# 			result.append(list( "".join(a) for a in permutations(s)))

	# 	else:
	# 		result.append(list( "".join(a) for a in permutations(s)))
	# ans = [[] for _ in range(len(result))]
	# for idx in range(len(result)):
	# 	for s in strs:
	# 		if s in result[idx]:
	# 			print(s, result[idx], idx)
	# 			ans[idx] += [s]
				
	
	# return ans

	## second
	# count = collections.Counter([tuple(sorted(s)) for s in strs])
	# return filter(lambda x: count[tuple(sorted(x))]>1, strs)

	d = {}
	for w in sorted(strs):
		key = tuple(sorted(w))
		d[key] = d.get(key, []) + [w]
	return list(d.values())

a = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupAnagrams(a))
