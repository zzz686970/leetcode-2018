# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def allPossibleFBT(self, N: 'int') -> 'List[TreeNode]':
        N -= 1
        if N == 0: return [TreeNode[0]]
        res = []
        for l in range(1, N, 2):
            for left in self.allPossibleFBT(l):
                for right in self.allPossibleFBT(N-l):
                    root = TreeNode(0)
                    root.left = left 
                    root.right = right 
                    res += [root]

        return res 


class Solution:
    def allPossibleFBT(self, N: 'int') -> 'List[TreeNode]':
        if N % 2 == 0: return [] # the number of node must be odd
        dp = [[] for _ in range(N+1)]
        dp[1] = [TreeNode(0)]
        for i in range(1, N+1, 2):
            for j in range(1, i, 2):
                for left in dp[j]:
                    for right in dp[i-1-j]:
                        node = TreeNode(0)
                        node.left = left
                        node.right = right
                        dp[i].append(node)
        return dp[N]

