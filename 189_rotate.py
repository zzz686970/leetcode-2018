class Solution(object):
	def rotate(self, nums, k):
		## way 1
		k = k % len(nums)
		nums[0: len(nums)-k] = nums[0: len(nums)-k][::-1]
		nums[len(nums)-k:] = nums[len(nums)-k:][::-1]
		nums[::] = nums[::-1]

		# return nums
		
		## way2
		# self.reverse(nums, 0, len(nums)-k-1)
		# self.reverse(nums, len(nums)-k, len(nums)-1)
		# self.reverse(nums, 0, len(nums)-1)

	def reverse(self, nums, start, end):
		while start < end:
			nums[start], nums[end] = nums[end], nums[start]
			start, end = start + 1, end - 1

a = Solution()
print(a.rotate([1,2,3,4,5,6,7], 3))