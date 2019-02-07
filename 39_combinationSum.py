import itertools 
# def combinationSum(candidates: 'List[int]', target: 'int') -> 'List[List[int]]':

# 	ans = []
# 	l = target // min(candidates) + 1
# 	for i in range(1, l):
# 		for c in itertools.combinations_with_replacement(candidates, i):
# 			if sum(c) == target:
# 				ans.append(list(c))
# 	return ans


## dfs way
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
