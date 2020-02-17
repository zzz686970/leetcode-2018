def reverse( x):
    """
    :type x: int
    :rtype: int
    """
    c = 0
    if x<0 and x> -(2 ** 31):
        c = int("-"+"".join(char for char in reversed(str(-x))))
        return c if c > -(2 ** 31) else 0

    elif x >= 0 and x < 2 ** 31 - 1:
        c =  int("".join(char for char in reversed(str(x))))
        return c if c < 2 ** 31 -1 else 0
    else:
        return 0

def reverse2(x):
    ans = int(str(x)[::-1]) if all([x>=0, x< 2 ** 31-1]) else (int("-" + str(x)[:0:-1])
        if all([x<0 , x> -(2 ** 31)])
        else 0)
    return ans if all([ans>=0, ans< 2 ** 31-1]) or all([ans<0 , ans> -(2 ** 31)]) else 0
print(reverse2(1534236469))

# 900000

# 1534236469
# 4294967296
# 9646324351