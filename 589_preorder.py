def preorder(root):
	result = []
	if not root: return result
	result.append(root.val)
	for child in root.children:
		result.extend(self.preorder(child))

	return result
