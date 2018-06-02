def selfDividingNumbers(left, right):
    """
    :type left: int
    :type right: int
    :rtype: List[int]
    """ 
    result = []
    for i in range(left, right+1):
        divider = [digit for digit in str(i)]
        if '0' not in divider and all(i % int(el) == 0 for el in divider):
            result.append(i)

    return result


        

print(selfDividingNumbers(1,22))