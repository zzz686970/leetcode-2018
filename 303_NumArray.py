class NumArray:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        # self.nums = nums
        self.accu = [0]
        for num in nums:
        	self.accu += self.accu[-1] + num,

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        # return sum(self.nums[i:j])
        return self.accu[j+1] - self.accu[i]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)