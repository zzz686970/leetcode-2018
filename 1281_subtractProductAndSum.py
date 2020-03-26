from operator import add, mul
from functools import reduce
def subtractProductAndSum(n):
	res = [int(el) for el in str(n)]
	# res = map(int, str(n))
	return reduce(mul, res) -  reduce(add, res)


def subtractProductAndSum_2(n):
    lookup = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    n_list = repr(n)
    sum_res, mul_res = 0, 1
    for c in n_list:
    	sum_res += lookup[c]
    	mul_res *= lookup[c]
    return mul_res - sum_res


if __name__ == '__main__':
	print(subtractProductAndSum_2(10))