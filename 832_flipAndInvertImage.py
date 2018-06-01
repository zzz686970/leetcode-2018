def flipAndInvertImage( A):
    """
    :type A: List[List[int]]
    :rtype: List[List[int]]
    """ 
    fliped = []
    inverted = []
    ## flip
    for ele in A:
        fliped.append(list(reversed(ele)))
    ## invert
    for ele in fliped:
        inverted.append([1 if char==0 else 0 for char in ele])

    return inverted

a = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
print(flipAndInvertImage(a))


