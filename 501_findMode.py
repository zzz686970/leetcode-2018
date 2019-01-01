class Solution:
	def findMode(self, root):
		"""
		:type root: TreeNode
		:rtype: List[int]
		"""
		## way1
		# import collections
		# if not root: return []
		# def in_order(node， cache):
		# 	if not node: return 
		# 	cache[root.val] += 1
		# 	in_order(node.left, cache)
		# 	in_order(node.right, cache)

		# cache = collections.defaultdict(int)
		# in_order(root, cache)
		# max_freq = max(cache.vaules())
		# return [k for k, v in cache.items() if v == max_freq]


from itertools import groupby
class Solution:
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ## two pass
        max_count = max((count for _, count in values_with_counts(root)), default=0)
        return [
            value
            for value, count in values_with_counts(root)
            if count == max_count
        ]
    
    
def values_with_counts(root):
    for value, iterator in groupby(in_order(root)):
        count = sum(1 for _ in iterator)
        yield value, count
    
    
def in_order(root):
    if root is not None:
        yield from in_order(root.left)
        yield root.val
        yield from in_order(root.right)

