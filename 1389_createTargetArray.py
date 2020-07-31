from typing import List
def createTargetArray(nums: List[int], index: List[int]) -> List[int]:
	target = []
	for a, b in zip(nums, index):
		target.insert(b, a)
	
	return target

## without insert
def createTargetArray(nums: List[int], index: List[int]) -> List[int]:
	target = []
	for i in range(len(index)):
		target = target[:index[i]] + [num[i]] + target[index[i]:]
	
	return target


## O(Nlog(n))

def createTargetArray(nums: List[int], index: List[int]) -> List[int]:
        def mergesort(index_pair):
            # each element is a pair of [old_idx, incremented_idx]
            if len(index_pair) < 2:
                return index_pair
            
            mid = len(index_pair) // 2
            left, right = mergesort(index_pair[:mid]), mergesort(index_pair[mid:])
            
            merge = []
            i = j = 0
            while i < len(left) and j < len(right):
                # as we're doing merge sort, `left` and `right` are sorted
                # we make sure at this moment, left[i][1] needs to at least increment j
                # therefore the actual value of left[i][1] now should be left[i][1] + j
                if left[i][1] + j >= right[j][1]:
                    merge.append(right[j])
                    j += 1
                else:
                    # we increment the offset when we merge it
                    left[i][1] += j
                    merge.append(left[i])
                    i += 1
            
            while i < len(left):
                left[i][1] += j # now j == len(right)
                merge.append(left[i])
                i += 1
            
            while j < len(right):
                merge.append(right[j])
                j += 1
            
            return merge
        
        index_pair = list(map(list, enumerate(index))) 
        merge = mergesort(index_pair)

        ans = [0] * len(nums)
        for orig_idx, new_idx in merge:
            ans[new_idx] = nums[orig_idx]
        
        return ans

print(createTargetArray(nums = [1,2,3,4,0], index = [0,1,2,2,1]))
print(createTargetArray([1,2,3,4,0], index = [0,1,2,3,0]))
print(createTargetArray(nums = [1], index = [0]))