class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        return len(set(sentence)) == 26
        # pool = {el:0 for el in string.ascii_lowercase}
        # for el in sentence:
        #     pool[el] += 1
        # return True if all(pool.values()) else False