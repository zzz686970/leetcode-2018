# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        stack = [(root, 0)]
        ans = 0
        while stack:
            node, visited = stack.pop()
            if not node: continue
            if visited == 0:
                stack.extend([(node.left, 0),(node, 1),(node.right, 0)])
            else:
                ans += node.val
                node.val = ans
        return root