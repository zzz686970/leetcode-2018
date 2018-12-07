class MyHashSet:

	def __init__(self):
		"""
		Initialize your data structure here.
		"""
		self.result = set()
		

	def add(self, key):
		"""
		:type key: int
		:rtype: void
		"""
		self.result.add(key)
		

	def remove(self, key):
		"""
		:type key: int
		:rtype: void
		"""
		if key in self.result:
			self.result.remove(key)

		

	def contains(self, key):
		"""
		Returns true if this set contains the specified element
		:type key: int
		:rtype: bool
		"""
		if key in self.result:
			return True
		return False
		


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)