def numMovesStones(a, b, c):
    ## re-order the value
    a, b, c  = sorted([a, b, c])
    ## case1: for any of the two numbers, the difference is 1
    if b-a == 1 or c-b == 1:
        ## case1.1 consecutive numbers already, eg 1,2,3
        if b-a == 1 and c-b==1:
            min_moves = 0
        ## case1.2 only partially cosecutive, eg 1,2,4
        else:
            min_moves =  1
    ## case2: for any of the two numbers, the difference is 2, meaning we can put the third number in between
    elif b-a == 2 or c-b == 2:
        min_moves = 1
    ## case3: for the general cases, we need at least 2 moves to form a consecutive array
    else:
        min_moves = 2

    ## max moves should be decreased by 1 at a time, hence (max_number - min_number - 2), eg 1,5,8--> 4,5,6 (1-->4, 8-->6)
    max_moves = c-a-2

    return [min_moves, max_moves]

print(numMovesStones(a = 3, b = 5, c = 1))
print(numMovesStones(a = 4, b = 3, c = 2))
print(numMovesStones(a = 1, b = 2, c = 5))
print(numMovesStones(a = 1, b = 3, c = 10))
# print(numMovesStones(a = 1, b = 2, c = 5))
# print(numMovesStones(a = 1, b = 2, c = 5))