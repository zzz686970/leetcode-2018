def getNoZeroIntegers(n):
    for i in range(1, n):
        # if '0' not in str(i) and '0' not in str(n-i):
        if '0' not in f'{i}{n-i}':
            return [i, n-i]

def getNoZeroIntegers(n):
    for a in range(n):
        if '0' not in f'{a}{n-a}':
            return [a, n-a]

def getNoZeroIntegers(n):
    a = 1
    while '0' in f'{a}{n-a}':
        a += 1
    return [a, n-a]

def getNoZeroIntegers(n):
    return next([a, n-a] for a in range(n) if '0' not in f'{a}{n-a}')    

if __name__ == '__main__':
    print(getNoZeroIntegers(2))
    print(getNoZeroIntegers(11))
    print(getNoZeroIntegers(10000))
    print(getNoZeroIntegers(1005))
    print(getNoZeroIntegers(69))
