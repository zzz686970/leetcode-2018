class MagicDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.res = {}

    def buildDict(self, dict):
        """
        Build a dictionary through a list of words
        :type dict: List[str]
        :rtype: void
        """
        for el in dict:
            self.res[len(el)] = self.res.get(len(el), []) + [el]
        

    def search(self, word):
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        :type word: str
        :rtype: bool
        """
        # if len(word) not in self.res: return False
        for pair in self.res.get(len(word),[]):
            total_diff = 0
            for a, b in zip(word, pair):
                if a != b:
                    total_diff += 1
                    if total_diff >=2:
                        break
            
            # for i in range(len(word)):
            #   if word[i] != pair[i]:
            #       total_diff += 1

            if total_diff == 1:
                return True 

        return False 


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dict)
# param_2 = obj.search(word)