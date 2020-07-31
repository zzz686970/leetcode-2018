# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        res, node_cnt = [[root.val]], 1
        stack = [root]
        
        while stack:
            ## pop out element in each level
            node = stack.pop(0)
            
            ## append left node
            if node.left:
                stack.append(node.left)
            
            ## append right node
            if node.right:
                stack.append(node.right)
            
            node_cnt -= 1
            ## node_cnt in each level equals to 0
            if node_cnt == 0:
                node_level = [el.val for el in stack]
                res += [node_level] if node_level else []
                node_cnt = len(stack)
        
        return res
            
        