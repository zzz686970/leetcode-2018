# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
        def sumEvenGrandparent(self, root: TreeNode) -> int:
            ans, queue = 0, collections.deque([(root, False)])
            while queue:
                parent, grandparent = queue.popleft()
                ## check whether current node is even valued
                evenparent = parent.val % 2 == 0
                for child in (parent.left, parent.right):
                    if child:
                        queue.append((child, evenparent))
                        ans += child.val if grandparent else 0

            return ans
            
            