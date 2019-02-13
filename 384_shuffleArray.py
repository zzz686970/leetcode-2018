from random import randint
class Solution:

    def __init__(self, nums: 'List[int]'):
        self.orig = [x for x in nums]
        self.nums = nums

    def reset(self) -> 'List[int]':
        """
        Resets the array to its original configuration and return it.
        """
        self.nums = [x for x in self.orig]
        return self.nums

    def shuffle(self) -> 'List[int]':
        """
        Returns a random shuffling of the array.
        """
        l, nums = len(self.nums), self.nums
        for i in range(l):
            j = randint(i, l-1)
            nums[i], nums[j] = nums[j], nums[i]

        return nums


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()