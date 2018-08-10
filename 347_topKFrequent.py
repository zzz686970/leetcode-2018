def topKFrequent(nums, k):
	## O(nlogn)
	# data , res = {}, []
	# for i in nums:
	# 	data[i] = data[i] + 1 if i in data else 1
	# sorted_data = sroted(data.iteritems(), key=operator.itemgetter(1), reverse=True)
	# for i in range(k):
	# 	res.append(sorted_data[i][0])
	# return res

	## most common
	# import collections
	# counter = collections.Counter(nums)
	# return [item[0] for item in counter.most_common(k)]

	## heapq
	# import heapq
	# data, res , pq = {}, [], []
	# for i in nums:
	# 	data[i] = data[i] +1 if i in data else 1
	# for key in data:
	# 	heapq.heappush(pq, (-data[key], key))
	# for i in range(k):
	# 	res.append(heapq.heappop(pd)[1])
	# return res
	
	import collections
	n = len(nums)
	cntDict = collections.defaultdict(int)
	for i in nums:
		cntDict[i] += 1
	freqList = [[] for i in range(n + 1)]
	for p in cntDict:
		freqList[cntDict[p]] += p,

	print(freqList)
	ans = []
	for p in range(n, 0, -1):
		ans += freqList[p]
	print(ans)
	return ans[:k]

nums = [1,1,1,2,2,3]
k = 2
print(topKFrequent(nums, k))
