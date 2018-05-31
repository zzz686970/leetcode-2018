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
