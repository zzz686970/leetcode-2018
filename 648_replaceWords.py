def replaceWords(dict, sentence):
	if not dict or not sentence: return sentence
	res = []
	pairs = sorted(dict, key=len)
	for word in sentence.split(' '):
		for pair in pairs:
			if pair in word[:len(pair)]:
				res.append(pair)
				break  
		else:
			res.append(word)

	return " ".join(res)

print(replaceWords(dict = ["cat", "bat", "rat"],
sentence = "the cattle was rattled by the battery"))

print(replaceWords(["a","b","c"],
"aadsfasf absbs bbab cadsfafs"))



def replaceWords(dict, sentence):
	res = {key: len(key) for key in dict}
	res_value = list(set(res.values()))
	res_value.sort()
	words = sentence.split(' ')
	for i, word in enumerate(words):
		for j in res_value:
			if word[:j] in res:
				words[i] = word[:j]
				break 

	return ' '.join(words)



## way 2 Trie
class TrieNode():
	def __init__(self):
		self.word = False
		self.children = {}

class Trie():
	def __init__(self):
		self.root = TrieNode()

	def insert(self, word):
		node = self.root 
		for i in word:
			if i not in node.children:
				node.children[i] = TrieNode()

			node = node.children[i]
		node.word = True 

	def find(self, word):
		node = self.root
		prefix = ''
		for i in word:
			prefix += i 
			if i not in node.children:
				return word 
			else:
				if node.children[i].word:
					return prefix 
				else:
					node = node.children[i]

		return word 

class Solution():
	def replaceWords(self, dict, sentence):
		trie = Trie()
		for i in dict:
			tire.insert(i)

		words = []
		for i in sentence.split(' '):
			words.append(tire.find(i))

		return ' '.join(words)
