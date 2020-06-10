from typing import List 

def countCharacters(words: List[str], chars: str) -> int:
    ans = 0
    res = collections.Counter(chars)
    for word in words:
        if all(res[k] >= v for k, v in collections.Counter(word).items()):
            ans += len(word)
    
    return ans
    
def countCharacters(words: List[str], chars: str) -> int:
    return sum(not cnt(w) - cnt(chars) and len(w) for w in words)