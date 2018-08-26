class Solution:
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        if root is None: return False
        bfs, s = [root], set()
        for i in bfs:
            if k - i.val in s: return True
            s.add(i.val)
            if i.left: bfs.append(i.left)
            if i.right: bfs.append(i.left)

        return False



