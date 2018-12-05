class MyHashMap:

	def __init__(self):
		"""
		Initialize your data structure here.
		"""
		self.data = {}
		

	def put(self, key, value):
		"""
		value will always be non-negative.
		:type key: int
		:type value: int
		:rtype: void
		"""
		self.key = key
		self.value = value
		self.data[self.key] = self.value

	def get(self, key):
		"""
		Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
		:type key: int
		:rtype: int
		"""

		return self.data.get(key,-1)
		

	def remove(self, key):
		"""
		Removes the mapping of the specified value key if this map contains a mapping for the key
		:type key: int
		:rtype: void
		"""
		if key in self.data:
			del self.data[key]
		else:
			return -1


# Your MyHashMap object will be instantiated and called as such:
obj = MyHashMap()
obj.put(1,2)
param_2 = obj.remove(2)
# obj.remove(key)