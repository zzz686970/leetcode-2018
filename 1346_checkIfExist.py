import collections
def checkIfExist(arr):
    res = collections.Counter(arr)
    ## if there are multiple zero elements in the list, return True
    if res[0] > 1: return True
    for el in arr:
        if res[2*el] and el != 0:
            return True 

    return False

def checkIfExist(arr):
    res = set()
    for el in arr:
        if (el % 2 == 0 and el // 2 in res) or el * 2 in res :
            return True 
        res.add(el)

    return False