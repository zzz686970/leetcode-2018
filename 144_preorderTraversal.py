# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """ 
        self.result = []
        self.dfs(root)
        return self.result

    def dfs(self, root):
        if not root:
            return 
        self.result.append(root.val)
        self.result.append(root.left)
        self.result.append(root.right)

    ## way 2
    result = []
    stack = [root]
    while stack:
        node = stack.pop()
        if node:
            result.append(node.val)
            stack.append(node.right)
            stack.append(node.left)
    return result

    ## way 3
    return [] if root is None else [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)
        