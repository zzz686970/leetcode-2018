# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        def dfs(node, lst):
            if node:
                lst.append(node)
                dfs(node.left, lst)
                dfs(node.right, lst)
         
        original_stack, cloned_stack = [], []
        dfs(original, original_stack)
        dfs(cloned, cloned_stack)
        
        for l1, l2 in zip(original_stack, cloned_stack):
            if l1 == target:
                return l2


    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        def find_node(orignal,copy,find):
            if not orignal:
                return None
            if orignal == find:
                return copy
            return find_node(orignal.left,copy.left, find) or find_node(orignal.right,copy.right,find)
        return find_node(original,cloned,target)


    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        def it(node):
            if node:
                yield node
                yield from it(node.left)
                yield from it(node.right)
            
        for n1, n2 in zip(it(original), it(cloned)):
            if n1 == target:
                return n2
        

        # if original == target:
        #     return cloned
        # stack = [(original, cloned)]
        # while stack:
        #     node1, node2 = stack.pop()
        #     if node1 == target:
        #         return node2
        #     if node1.right:
        #         stack.append((node1.right, node2.right))
        #     if node1.left:
        #         stack.append((node1.left, node2.left))                