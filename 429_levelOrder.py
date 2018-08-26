"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if not root: return []
        result = []
        stack = [root]
        while stack:
            tmp = []
            next_stack = []
            for node in stack:
                tmp.append(node.val)
                for child in node.children:
                    next_stack.append(child)
            stack = next_stack
            result.append(tmp)
        
        return result