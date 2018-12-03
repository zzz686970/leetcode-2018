# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        ## for the current node with the most path
        path = [0]
        def traverse(node):
            if not node: return 0
            l_len, r_len = traverse(node.left), traverse(node.right)
            l = (l_len + 1) if node.left and node.left.val == node.val else 0
            r = (r_len + 1) if node.right and node.right.val == node.val else 0
            path[0] = max(path[0], l+r)

            ## return the value of each node, for the leaf, it is 0
            return max(l, r)

        traverse(root)
        return path[0]