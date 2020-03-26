def relativeSortArray(arr1, arr2):
	k = {v: idx for idx, v in enumerate(arr2)}
	return list(sorted(arr1, key=lambda x: k.get(x, x + 1000)))