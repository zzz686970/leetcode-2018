def sortedArrayToBST(nums):
	if len(nums):
		head = TreeNode(nums[len(nums)//2])
		head.left = self.sortedArrayToBST(nums[:len(nums)//2])
		head.right = self.sortedArrayToBST(nums[len(nums)//2+1:])
	else:
		head = None

	return head