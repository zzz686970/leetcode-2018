# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import collections
class Solution:
    ## dfs + stack
    def sumNumbers(self, root: TreeNode) -> int:
        if not root: return 0
        stack, res = [(root, root.val)], 0
        while stack:
            node, val = stack.pop()
            if node:
                if node.right:
                    stack.append((node.right, val * 10 + node.right.val))
                ## append at last because we pop first
                if node.left:
                    stack.append((node.left, val * 10 + node.left.val))
                if not node.left and not node.right:
                    res += val
        return res


    ## bfs + queue
    def sumNumbers2(self, root):
        if not root:
            return 0 

        queue, res = collections.deque([(root, root.val)]), 0
        while queue:
            node, val = queue.popleft()
            if node:
                if not node.left and not node.right:
                    res += val 
                if node.left:
                    queue.append((node.left, val * 10 + node.left.val))
                if node.right:
                    queue.append((node.right, val * 10 + node.right.val))

        return res 

    ## recursive
    def sumNumbers(self, root):
        self.res = 0
        self.dfs(root, 0)
        return self.res 

    def dfs(self, root, value):
        if root:
            self.dfs(root.left, value * 10 + root.left.val)

            self.dfs(root.right, value * 10 + root.right.val)

            if not root.left and not root.right:
                self.res += value * 10 + root.val

