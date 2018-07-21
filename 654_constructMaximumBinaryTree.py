# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None

        i = nums.index(max(nums))
        node = TreeNode(nums[i])

        node.left = self.constructMaximumBinaryTree(nums[:i])
        node.right = self.constructMaximumBinaryTree(nums[i + 1:])

        return node
        
