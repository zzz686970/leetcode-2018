from typing import List 

def mostVisited(n: int, rounds: List[int]) -> List[int]:
    ## if start <= end, return range(start, end+1)
    ## if end < start, return range(1, end+1) + range(start, n+1)
    return range(A[0], A[-1] + 1) or range(1, A[-1]+1) + range(A[0], n + 1)

def mostVisited(n: int, rounds: List[int]) -> List[int]:
    res = [0] * n
    for i in range(1, len(rounds)):
        start, end = rounds[i-1], rounds[i]
        if i == 1:
            if start < end:
                res[start-1: end] = [x+1 for x in res[start-1:end]]
            else:
                res[start-1:] = [x+1 for x in res[start-1:]]
                res[:end] = [x+1 for x in res[:end]]
        else:
            if start < end:
                res[start: end] = [x+1 for x in res[start:end]]
            else:
                res[start:] = [x+1 for x in res[start:]]
                res[:end] = [x+1 for x in res[:end]]
            
    return [i+1 for i in range(len(res)) if res[i] == max(res)]

if __name__ == '__main__':
    print(mostVisited(n = 4, rounds = [1,3,1,2]))
    print(mostVisited(n = 2, rounds = [2,1,2,1,2,1,2,1,2]))
    print(mostVisited(n = 7, rounds = [1,3,5,7]    ))