import itertools
class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.iterator_list = list(itertools.combinations(characters, combinationLength))

    def next(self) -> str:
        if len(self.iterator_list):
            return "".join(self.iterator_list.pop(0))
        

    def hasNext(self) -> bool:
        if len(self.iterator_list):
            return True
        else:
            return False
        


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()