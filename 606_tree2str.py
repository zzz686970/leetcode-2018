class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

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
                result += "()"

            ## right was first so pop later
            if node.right:
                stack.append(")")
                stack.append(node.right)

            ## left needs to be popped first=
            if node.left:
                stack.append(")")
                stack.append(node.left)

        return result[1:]

node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)

node1.left = node2 
node2.left = node4 
node1.right = node3 


print(Solution.tree2str(None, node1))
