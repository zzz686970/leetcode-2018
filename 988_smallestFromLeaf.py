class solution():
	def smallestFromLeaf(self, root: 'TreeNode') -> 'str':
		if not root: return ''
		left = self.smallestFromLeaf(root.left)
		right = self.smallestFromLeaf(root.left)

		return (left if right == '' or (left != '' and left < right) else right) + chr(97 + root.val )


## dfs 

class solution():
	def smallestFromLeaf(self, root: 'TreeNode') -> 'str':
		if not root: return ''

		s = []
		def dfs(root, lst):
			if not root.left and not root.right:
				s.append(''.join([chr(root.val + 97)] + lst))
				return 

			if root.left: dfs(root.left, [chr(root.val + 97) + lst])
			if root.right: dfs(root.right, [chr(root.val+97) + lst])

		dfs(root, [])

		return list(sorted(s))[0]


class solution():
	def smallestFromLeaf(self, root: 'TreeNode') -> 'str':
		def dfs(node):
			if not node:
				return 
			l, r = dfs(node.left), dfs(node.right)
			cur = chr(node.val + 97)
			if not l and not r:
				return chr(node.val + 97)
			if not l:
				return r + cur 
			if not r:
				return l + cur 

			return min(l+cur, r+cur)

		return dfs(root)
		

