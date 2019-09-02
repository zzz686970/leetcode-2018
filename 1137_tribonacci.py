import functools
from time import time

def tribonacci(n):
	a, b, c = 0, 1, 1
	for _ in range(n):
		a, b, c = b, c, a+b+c
	return a


## maximum recursion depth exceeded
def fibs(n):
	fibs = [0, 1, 1]
	for i in range(3, n+1):
		fibs.append(fibs[-1] + fibs[-2] + fibs[-3])

	return fibs[n]


## maximum recursion depth exceeded
## save computed value in a dict to prevent re-compute
# def fib_memo(n, computed={0:0,1:1,2:1}):
# 	if n not in computed:
# 		computed[n] = fib_memo(n-1, computed) + fib_memo(n-2, computed) + fib_memo(n-3, computed)
# 	return computed[n]


## decorator
@functools.lru_cache(None)
def fib_lru(n):
	if n < 3:
		return n
	return fibs(n-1) + fibs(n-2) + fibs(n-3)



## maximum recursion depth exceeded
# def fib_local(n):
# 	computed = {0 : 0, 1 : 1, 2 : 1}
# 	def fib_inner(n):
# 		if n not in computed:
# 			computed[n] = fib_inner(n-1) + fib_inner(n-2) + fib_inner(n-3)
# 		return computed[n]
# 	return fib_inner(n)


## maximum recursion depth exceeded
# def fib_local_exc(n):
# 	computed = {0: 0, 1: 1, 2:1}
# 	def fib_inner_x(n):
# 		try:
# 			computed[n]
# 		except KeyError:
# 			computed[n] = fib_inner_x(n-1) + fib_inner_x(n-2) + fib_inner_x(n-3)
# 		return computed[n]

# 	return fib_inner_x(n)


# benchmark test:
def benchmark(n, *args):
	print("-" * 80)
	for func in args:
		print(func.__name__)
		start = time()
		try:
			ret = func(n)
			#print("Result:", ret)
		except RuntimeError as e:
			print("Error:", e)
		print("Time:", "{:.8f}".format((time() - start)*1000) + 'ms' )
		print()

benchmark(10000, tribonacci,fib_lru)