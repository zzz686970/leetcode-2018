def arrayRankTransform(arr):
	# rank = {}
	# for a in sorted(arr):
	# 	rank.setdefault(a, len(rank) +1)
	# return map(rank.get, arr)
	
	return list(map({el:i+1 for i, el in enumerate(sorted(set(arr)))}.get, arr))

if __name__ == '__main__':
	print(arrayRankTransform(arr = [40,10,20,30]))