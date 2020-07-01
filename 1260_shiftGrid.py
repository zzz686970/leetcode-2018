def shiftGrid(grid, k):
    # sum() takes two parameters iterable and start,i.e.,sum(iterable,start)
    # by default start=0. so we cannot concatenate a list and integer,that why we are taking start=[ ] empty list
    m, n = len(grid), len(grid[0])
    ## flatten the 2-d list
    res = sum(grid, [])
    ## if need to shift multiple times, use mod if k is larger then length of m * n 
    k = k % len(res)
    ## shift function, choose the last k elements and put them in the head
    res = res[-k:] + res[:-k] 
    ## revert back to nested list
    # return list(map(lambda x: res[m*x:(x+1)*m], range (n)))
    return [res[i*n:(i+1) * n] for i in range(m)]

if __name__ == '__main__':
    # print(shiftGrid(grid = [[1,2,3],[4,5,6],[7,8,9]], k = 1))
    # print(shiftGrid([[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]],4))
    print(shiftGrid([[1],[2],[3],[4],[7],[6],[5]],23))

