class KthLargest:

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.k = k
        self.nums = nums
        heapq.heapify(self.nums)
        while len(self.nums) > k:
        	heapq.heappop(self.nums)

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        if len(self.nums) < self.k:
        	heapq.heappush(self.nums, val)
        else:
        	heapq.heappushpop(self.nums, val)

        return self.nums[0]
        # self.nums.append(val)

        ## time limit
        # return list(sorted(self.nums)[::-1])[self.k]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)