import heapq
def lastStoneWeight(stones):
	arr = [-el for el in stones]
	heapq.heapify(arr)
	while len(arr) > 1:
		x, y = heapq.heappop(arr), heapq.heappop(arr)
		if abs(x - y) != 0:
			heapq.heappush(arr, -abs(x - y) )

	return -arr[0] if arr else 0

print(lastStoneWeight(stones = [2,7,4,1,8,1]))

