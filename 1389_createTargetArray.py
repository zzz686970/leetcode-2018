from typing import List
def createTargetArray(nums: List[int], index: List[int]) -> List[int]:
	target = []
	for a, b in zip(nums, index):
		target.insert(b, a)
	
	return target

print(createTargetArray(nums = [1,2,3,4,0], index = [0,1,2,2,1]))
print(createTargetArray([1,2,3,4,0], index = [0,1,2,3,0]))
print(createTargetArray(nums = [1], index = [0]))