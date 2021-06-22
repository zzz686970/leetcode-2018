class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        return all(c1 == c2 for c1, c2 in zip(self.gen(word1), self.gen(word2)))

    def gen(self, words):
        for word in words:
            for s in word:
                yield s 

        yield None  



if __name__ == '__main__':
    print(arrayStringsAreEqual(["jbboxe","yshcrtanrtlzyyp","vudsssnzuef","lde"],
["jbboxeyshcrtanrt","lzyypvudsssnzueflde"]))

    print(["a", "cb"], ["ab", "c"])