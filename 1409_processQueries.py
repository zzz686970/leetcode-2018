from typing import List 

def processQueries(queries: List[int], m: int) -> List[int]:
    p = list(range(1, m+1))
    for i, el in enumerate(queries):
        queries[i] = p.index(el)
        p.insert(0, p.pop(queries[i]))
    
    return queries