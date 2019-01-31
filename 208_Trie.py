class Trie(object):

	def __init__(self):
		"""
		Initialize your data structure here.
		"""
		self.trie = {}

	def insert(self, word):
		"""
		Inserts a word into the trie.
		:type word: str
		:rtype: void
		"""
		t = self.trie 
		for w in word:
			if w not in t:
				t[w] = {}
			t = t[w]

		t['#'] = '#'

	def search(self, word):
		"""
		Returns if the word is in the trie.
		:type word: str
		:rtype: bool
		"""
		t = self.trie 
		for w in word:
			if w not in t:
				return False 
			t = t[w]

		if '#' in t:
			return True 
		return False 

	def startsWith(self, prefix):
		"""
		Returns if there is any word in the trie that starts with the given prefix.
		:type prefix: str
		:rtype: bool
		"""
		t = self.trie 
		for w in prefix:
			if w not in t:
				return False 
			t = t[w]

		return True 


import collections
from functools import reduce
class Trie(object):

	def __init__(self):
		"""
		Initialize your data structure here.
		"""
		T = lambda: collections.defaultdict(T)
		self.root = T()

	def insert(self, word):
		"""
		Inserts a word into the trie.
		:type word: str
		:rtype: void
		"""
		reduce(dict.__getitem__, word, self.root)['#'] = True 

	def search(self, word):
		"""
		Returns if the word is in the trie.
		:type word: str
		:rtype: bool
		"""
		return '#' in reduce(lambda cur, c:cur.get(c, {}), word, self.root)


	def startsWith(self, prefix):
		"""
		Returns if there is any word in the trie that starts with the given prefix.
		:type prefix: str
		:rtype: bool
		"""
		return bool(reduce(lambda cur, c: cur.get(c, {}), prefix, self.root))




## way 3
import collections
from functools import reduce
class TrieNode():
	def __init__(self):
		self.children = collections.defaultdict(TrieNode())
		self.is_word = False

class Trie(object):

	def __init__(self):
		"""
		Initialize your data structure here.
		"""
		self.root = TrieNode()

	def insert(self, word):
		"""
		Inserts a word into the trie.
		:type word: str
		:rtype: void
		"""
		cur = self.root 
		for w in word:
			cur = cur.children[w]
		cur.is_word = True 

	def search(self, word):
		"""
		Returns if the word is in the trie.
		:type word: str
		:rtype: bool
		"""
		cur = self.Trie()
		for w in word:
			## if w not in cur.children:  return False
			## cur = cur.children[w]
			cur = cur.children.get(w) 
			if cur is None:
				return False

		return cur.is_word

	def startsWith(self, prefix):
		"""
		Returns if there is any word in the trie that starts with the given prefix.
		:type prefix: str
		:rtype: bool
		"""
		cur = self.root 
		for w in prefix:
			## if w not in cur.children: return False
			## cur = cur.children[w]
			cur = cur.children.get(w)

			if cur is None:
				return False 

		return True 



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)


# trie = {}

# def insert(word):
# 	t = trie
# 	for w in word:
# 		if w not in t:
# 			t[w] = {}

# 		t = t[w]
# 	t['#'] = '#'

# insert('apple')
# insert('app')
# print(trie)
