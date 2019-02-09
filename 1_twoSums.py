def twoSum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(len(nums)-1,0, -1):
                if i != j:
                    if nums[i] + nums[j] == target:
                        return [i, j]
                else:
                    break
            


nums = [2, 7, 11, 15]
target = 22
twoSum(nums, target)


def find_pairs(nums, target):
    # ans = []
    # for i in range(len(nums)-1):
    #     for j in range(i+1, len(nums)):
    #         if nums[i] + nums[j] == target:
    #             ans += (nums[i], nums[j]),

    # return ans 

    ## O(nlog(n))
    nums.sort()
    ans = []
    l, r = 0, len(nums) - 1
    while l < r:
        if nums[l] + nums[r] == target:
            ans.append((nums[l], nums[r]))
            l += 1
            r -= 1

        elif nums[l] + nums[r] > target:
            r -= 1
        else:
            l += 1

    return ans 

print(find_pairs([1,3,2,5,7,44, 6], 7))
