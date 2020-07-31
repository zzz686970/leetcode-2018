def isPathCrossing(path: str) -> bool:
    directions = {'N': [0,1], 'S': [0, -1], 'E': [1, 0], 'W': [-1, 0]}
    res = [[0,0]]
    cur = (0, 0)
    for direction in path:
        cur = [sum(el) for el in [*zip(cur, directions[direction])]]
        if curin res:
            return True 
        res.append(cur)
    return False 

import operator
def isPathCrossing(path: str) -> bool:
    cur = (0, 0)
    seen = {cur}
    direction = {'N': (0, 1), 'S': (0, -1), 'E': (1, 0), 'W': (-1, 0)}
    for char in path:
        cur = tuple(map(operator.add, cur, direction[char]))
        if cur in seen:
            return True
        seen.add(cur)
    return False

if __name__ == '__main__':
    print(isPathCrossing(path = "NES"))
    print(isPathCrossing(path = "NESWW"))