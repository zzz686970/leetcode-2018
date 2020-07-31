from typing import List 
def maxProbability(n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
	def dfs():
		pass

	# edges = sorted(edges, key = lambda x: x[0]) 
	res = []
	dfs(edges, 0, )




def combinationSum(candidates, target):
	def dfs(nums, target, index, path, res):
		if target < 0:
			return 
		if target == 0:
			res.append(path)
			return 

		## no need to return
		for i in range(index, len(nums)):
			dfs(nums, target-nums[i], i, path+[nums[i]], res)

	res = []
	candidates.sort()
	dfs(candidates, target, 0, [], res )
	return res 


print(combinationSum(candidates = [2,3,5], target = 8))

if __name__ == '__main__':
	assert 0.25 == maxProbability(n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.2], start = 0, end = 2)
	assert 0.3 == maxProbability(n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.3], start = 0, end = 2)
	assert 0 == maxProbability(n = 3, edges = [[0,1]], succProb = [0.5], start = 0, end = 2)
	
