def findSolution(customfunction, z):
    res = []
    y = 1000
    for x in range(1, 1001):
        while y >= 1 and customfunction.f(x, y)  > z:
            y -= 1

        ## stop iterating if y = 0
        if y == 0:
            break 

        if customfunction.f(x, y) == z:
            res.append([x, y])

    return res


