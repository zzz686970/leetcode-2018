from decimal import Decimal
import timeit
import time 

def fun(n):
    ## 1 1
    ## 2 1
    ## 3 2
    ## 4 1+3 3+1 --> 3
    ## 5 1+4 3+2 --> 4
    ## 6 1+5 3+3 --> 6
    ## 7 1+6 3+4 --> 9
    ## 8 1+7 3+5 --> 13
    ## 9 1+8 3+6 --> 19
    if n == 0: return 1
    elif n == 1: return 1
    elif n == 2: return 2
    else:
        return int((fun(n-1) + fun(n-3)) % (1e9+7))

def fun2(n):
    ## 1 1
    ## 2 1
    ## 3 2
    ## 4 1+3 3+1 --> 3
    ## 5 1+4 3+2 --> 4
    ## 6 1+5 3+3 --> 6
    ## 7 1+6 3+4 --> 9
    ## 8 1+7 3+5 --> 13
    ## 9 1+8 3+6 --> 19
    a, b, c = 1,1,2
    if n == 0: return 1
    elif n == 1: return 1
    elif n == 2: return 2
    else:
        for i in range(2, int(n)):
            a, b, c = b, c, a+c
        return c % int(1e9+7)

if __name__ == '__main__':
    start = time.time()
    print(fun2(int(1e6)))
    end = time.time()
    print ("Took %f ms" % ((end - start) * 1000.0))
    t1 = timeit.Timer("func2(int(1e5))", "from __main__ import func2")
    # print("fun2 ran:",t1.timeit(number=1000), "milliseconds")
    # print(fun2(1e5), timeit.timeit(fun2(1e5)))
