def countNegatives(grid):
	## O(M*N) ==> O(N^2)
    return sum(el < 0 for row in grid for el in row)
    # return str(grid).count('-')
    # return (np.array(grid) < 0).sum()
	# return sum([grid[i][j] < 0 for i in range(len(grid)) for j in range(len(grid[0]))])


# O(NlogN)
def countNegatives(grid):
    return sum(bisect_left(type('', (), {'__getitem': lambda _,  i: r[~]})(), 0, 0, len(r)) for r in grid)

def binarySearch(row):
    left = 0
    right = len(row)-1
    length = len(row)

    if(row[0] < 0):
        return (length)

    while(right >= left):
        mid = int(left + (right-left)/2)
        if(row[mid] >= 0 and mid != length-1 and row[mid+1] < 0):
            return length-mid-1
        elif(row[mid] < 0 and row[mid+1] < 0):
            right = mid-1
        else:
            left = mid+1

    return 0

## O(nlogn)
def countNegatives(grid: List[List[int]]) -> int:

    count = 0
    for row in grid:
        count += binarySearch(row)
    return count



import bisect
def countNegatives(grid):
	return sum(bisect_left(type('', (), {'__getitem__': lambda _, i: r[~i]})(), 0) for r in grid)
	return(j:=0)or sum((j:=next((j for j in range(j,len(r))if r[~j]>=0),len(r)))for r in A)
	return sum(itertools.accumulate([0]+A,lambda j,r:next((j for j in range(j,len(r))if r[~j]>=0),len(r))))


if __name__ == '__main__':
	print(countNegatives(grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]))
	# print(countNegatives(grid = [[3,2],[1,0]]))
	# print(countNegatives(grid = [[1,-1],[-1,-1]]))
	# print(countNegatives(grid = [[-1]]))

# 8
# 0
# 3
# 1