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

print(reverse(1534236469))

# 900000

# 1534236469
# 4294967296
# 9646324351