def convertToBase7(num):
	## time out
    # a = 0
    # i = 0
    # while num:
    #     num,r = divmod(num,7)
    #     a += 10**i * r
    #     i += 1
    # return a
    if num == 0: return '0'
    n, res = abs(num), ''
    while n:
      res = str(n % 7) + res
      n //= 7
    return res if num > 0 else '-' + res

print(convertToBase7(-7))