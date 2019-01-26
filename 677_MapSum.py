class MapSum:

	def __init__(self):
		"""
		Initialize your data structure here.
		"""
		self.res = {}

	def insert(self, key, val):
		"""
		:type key: str
		:type val: int
		:rtype: void
		"""
		self.res[key] = val
		# if key not in self.res:
		# 	self.res[key] = val 
		# else:
		# 	self.res[key] = val 

	def sum(self, prefix):
		"""
		:type prefix: str
		:rtype: int
		"""
		ans = 0
		for key, val in self.res.items():
			if prefix in key[:len(prefix)]:
				ans += val 

		return ans

		## return sum(self.res[i] for i in self.res if i.startswith(prefix) or [0])

# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)

class TrieNode():
	def __init__(self, count=0):
		self.count = count 
		self.children = {}

class MapSum2:
	## construct a trie

	def __init__(self):
		"""
		Initialize your data structure here.
		"""
		self.root = TrieNode()
		self.keys = {}

	def insert(self, key, val):
		"""
		:type key: str
		:type val: int
		:rtype: void
		"""
		delta = val - self.keys.get(key, 0)
		self.keys[key] = val 

		curr = self.root 
		curr.count += delta 
		for char in key:
			if char not in curr.children:
				curr.children[char] = TrieNode()
			curr = curr.children[char]
			curr.count += delta 

	def sum(self, prefix):
		"""
		:type prefix: str
		:rtype: int
		"""
		curr = self.root 
		for char in prefix:
			if char not in curr.children:
				return 0
			curr = curr.children[char]
		return curr.count 

# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)


