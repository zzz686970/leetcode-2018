def threeConsecutiveOdds(arr):
	return any([False if i < 2 else arr[i-2] & arr[i-1] & arr[i] & 1 for i in range(len(arr))])