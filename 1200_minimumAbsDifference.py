import collections
def minimumAbsDifference(arr):
	arr.sort()
	mx = float('inf')
	ans = collections.defaultdict(list)
	for i in range(1, len(arr)):
		if abs(arr[i-1] - arr[i]) <= mx:
			mx = abs(arr[i-1] - arr[i])
			ans[mx].append([arr[i-1], arr[i]])
	
	return ans[mx]

# def minimumAbsDifference(arr):
# 	arr.sort()
# 	mn = min(b - a for a, b in zip(arr, arr[1:]))
#     return [[a, b] for a, b in zip(arr, arr[1:]) if b - a == mn] 

if __name__ == '__main__':
	print(minimumAbsDifference(arr = [4,2,1,3]))