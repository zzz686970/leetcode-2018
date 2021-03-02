from typing import List
import itertools

def canFormArray(arr: List[int], pieces: List[List[int]]) -> bool:
    for piece in pieces:
        if piece[0] not in arr:
            return False
        else:
            if len(piece) > 1 and any(a != b for a, b in itertools.zip_longest(piece, arr[arr.index(piece[0]):len(piece)+arr.index(piece[0])])):
                return False
    
    return True
def canFormArray(arr: List[int], pieces: List[List[int]]) -> bool:
    arr_str = "!".join(map(str, arr)) + "!"
    return all("!".join(map(str, p)) + "!" in arr_str for p in pieces)

def canFormArray(arr: List[int], pieces: List[List[int]]) -> bool:
    d = {x[0]: x for x in pieces}
    return list(chain(*[d.get(num, []) for num in arr])) == arr
 
if __name__ == '__main__':
    print(canFormArray(
[2,82,79,95,28], [[2],[82],[28],[79,95]]))