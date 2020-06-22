from typing import List
def stringMatching(words):
    ans = "  ".join(words)
    return [el for el in words if ans.count(el) >= 2]


def stringMatching(words: List[str]) -> List[str]:
    def add(word: str):
        node = trie
        for c in word:
            node = node.setdefault(c, {})
            node['#'] = node.get('#', 0) + 1

    def get(word: str) -> bool:
        node = trie
        for c in word:
            node = node.get(c)
            if node is None: return False
            # if (node := node.get(c)) is None: return False
        return node['#'] > 1

    trie = {}
    for word in words:
        for i in range(len(word)):
            add(word[i:])
    print(trie)
    return [word for word in words if get(word)]

if __name__ == '__main__':
    print(stringMatching(words = ["mass","as","hero","superhero"]))
    print(stringMatching(words = ["leetcoder","leetcode","od","hamlet","am"]))