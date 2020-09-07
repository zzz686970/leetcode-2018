from typing import List
import bisect 

def insert(intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    bisect.insort(intervals, newInterval)
    res = [intervals[0]]
    for el in intervals:
        if el[0] > res[-1][1]:
            res.append(el)
        else:
            # res[-1][0] = min(el[0], res[-1][0])
            res[-1][1] = max(el[1], res[-1][1])
    
    return res

if __name__ == '__main__':
    print(insert(intervals = [[1,3],[6,9]], newInterval = [2,5]))
    print(insert(intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]))