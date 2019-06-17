def networkDelayTime(times, N, K):
	def bellmenford(times, N, K):
		graph = {}
		for u,v, w in times:
			if u not in graph:
				graph[u] = [(v, w)]
			else:
				graph[u].append((v,w))

		dist = {node: float('inf') for node in range(1, N+1)}
		dist[K] = 0

		def relax(u, v, w):
			if dist[v] > dist[u] + w:
				dist[v] = dist[u] + w

		for _ in range(N-1):
			for i in graph:
				for v, w in graph[i]:
					relax(i, v, w)

		ans = max(dist.values())
		return ans if ans < float('inf') else -1

def dijkstra(times, N, K):

	import collections
	import heapq
	graph = collections.defaultdict(list)
	for u, v, w in times:
		graph[u].append((v, w))

	q, visited = [(0,K)], {}
	while q:
		time, node = heapq.heappop(q)
		if node not in visited:
			visited[node] = time
			for v, w in graph[node]:
				heapq.heappush(q, (time+w, v))

	print(visited)
	return max(visited.values()) if len(visited) == N else -1

print(dijkstra(times = [[2,1,3],[2,3,1],[3,4,4], [2,4,1], [1,5,8], [4,5,3]], N = 5, K = 2))


