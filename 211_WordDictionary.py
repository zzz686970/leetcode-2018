import collections
class TrieNode():
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.is_word = False 

class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        cur = self.root 
        for w in word:
            cur = cur.children[w]

        cur.is_word = True

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        cur = self.root 
        for w in word:
            if w == '.':
                continue 

            elif w not in cur.children:
                return False

            if w == '.':
                for char in cur.children:
                    cur = cur.children[char]
            else:
                cur = cur.children[w] 

        return cur.is_word
        


import collections
class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        cur = self.root 
        for w in word:
            cur = cur.children[w]

        cur.is_word = True

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        cur = self.root 
        for w in word:
            if w == '.':
                continue 

            elif w not in cur.children:
                return False

            if w == '.':
                for char in cur.children:
                    cur = cur.children[char]
            else:
                cur = cur.children[w] 

        return cur.is_word

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)