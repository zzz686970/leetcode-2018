# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.ans = 0

    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def depth(p):
            if not p: return 0
            left, right = depth(p.left), depth(p.right)
            self.ans = max(self.ans, left + right)

            return 1 + max(left, right)

        depth(root)

        return self.ans


result = []
node = ["node" + str(i + 1) for i in range(5)]
node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)

node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5

a = Solution()
print(a.diameterOfBinaryTree(node1))
