class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        if not t: return ""
        stack = [t]
        result = ""
        while stack:
            node = stack.pop()
            if node == ")":
                result += ")"
                continue
            result += "(" + str(node.val)

            if not node.left and node.right:
                res += "()"
            if node.right:
                stack.append(")")
                stack.append(node.right)
            if node.left:
                stack.append(")")
                stack.append(node.left)

        return result[1:]

tree = TreeNode()

print(tree.tree2str([1,2,3,4]))
