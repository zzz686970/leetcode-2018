# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

## dfs O(n)
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        stack = [(root, 0)]
        max_level, res = -1, 0
        while stack:
            node, level = stack.pop()
            if node.right:
                stack.append((node.right, level+1))
            if node.left:
                stack.append((node.left, level+1))
            if not node.right and not node.left:
                if level > max_level:
                    max_level = level
                    res = node.val
                elif level == max_level:
                    res += node.val
        
        return res

    def deepestLeavesSum(self, root: TreeNode) -> int:
        if not root: return 0
        last_layer, layer = [], [root]
        while layer:
            last_layer, layer = layer, [child for node in layer for child in (node.left, node.right) if child]

        return sum(node.val for node in last_layer)

## bfs O(n)
