# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def printTree(self, root: 'TreeNode') -> 'List[List[str]]':
        """[summary]
        
        Two pass
        1. dfs to get length of the tree
        2. traverse the tree again, binary find, root --> mid
        
        Arguments:
            root: 'TreeNode' {[type]} -- [description]
        """ 
        def get_height(root):
            return 0 if not root else 1+max(get_height(root.left), get_height(root.right))

        def binary_find(node, level, left, right):
            if not node: return 

            mid = (left + right) // 2
            self.res[level][mid] = str(node.val)
            binary_find(node.left, level+1,  left, mid-1)
            binary_find(node.right, level+1, mid+1, right)

        height = get_height(root)
        width = 2 ** height -1 
        self.res = [[''] * width for i in range(height)]
        binary_find(root, 0, 0, width-1)
        return self.res 