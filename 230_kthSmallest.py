# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        cur, stack = root, []
        ## cur is current node, stack store in-order node
        while cur or stack:
            if cur:
                stack.append(cur)
                cur = cur.left
            ## cur becomes None due to cur.left or cur.right
            ## check stack to see whether k-th element is in the current stack
            elif len(stack):
                cur = stack.pop()
                k -= 1
                if k == 0:
                    return cur.val 
                cur = cur.right 

            else:
                break 
        return -1 

