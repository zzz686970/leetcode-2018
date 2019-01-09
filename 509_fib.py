# def fib(N, cache = {}):
# 	if N == 0: return 0
# 	if N == 1: return 1
# 	a, b = 0, 1
# 	for i in range(N):
# 		a, b = b, a+b 

# 	return a

"""Fib

Some ways to compute fibs
"""
import functools
from time import time

def fibs(n):
	fibs = [0, 1]
	for i in range(2, n+1):
		fibs.append(fibs[-1] + fibs[-2])

	return fibs

## save computed value in a dict to prevent re-compute
def fib_memo(n, computed={0:0,1:1}):
	if n not in computed:
		computed[n] = fib_memo(n-1, computed) + fib_memo(n-2, computed)
	return computed[n]

## decorator
@functools.lru_cache(None)
def fib_lru(n):
	if n < 2:
		return n
	return fibs(n-1) + fibs(n-2)

## count up
def fib_iter(n):
	a, b = 0, 1
	for _ in range(n):
		a, b = b, a+b
	return n

## bit ops
def fib_bits(n):
	if n == 0: return 0
	v1, v2, v3 = 1,1,0
	for rec in bin(n)[3:]:
		calc = v2 * v2
		v1, v2, v3 = v1*v1 + calc, (v1+v3) * v2, calc + v3 * v3
		if rec=='1': v1, v2, v3 = v1+v2, v1, v2
	return v2
# for i in range(10):
# 	print(fib_bits(i))

def fib_local(n):
	computed = {0: 0, 1: 1}
	def fib_inner(n):
		if n not in computed:
			computed[n] = fib_inner(n-1) + fib_inner(n-2)
		return computed[n]
	return fib_inner(n)

def fib_local_exc(n):
	computed = {0: 0, 1: 1}
	def fib_inner_x(n):
		try:
			computed[n]
		except KeyError:
			computed[n] = fib_inner_x(n-1) + fib_inner_x(n-2)
		return computed[n]

	return fib_inner_x(n)

def fib_o1(n):
	return round(((1+5 ** 0.5) / 2 )**n / (5 ** 0.5))


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

benchmark(500, fib_iter, fib_o1, fib_bits,   fib_memo, fib_local, fib_local_exc, fib_lru)




def fib(self, N):
	"""
	:type N: int
	:rtype: int
	"""
	a, b = 0, 1
	for _ in range(N):
		a, b = b, a+b 

	return a

def fib_o1(n):
	return round(((1+5 ** 0.5) / 2 )**N / (5 ** 0.5))

def fib_bits(n):    
	if N == 0: return 0
	v1, v2, v3 = 1,1,0
	for rec in bin(N)[3:]:
		calc = v2 * v2
		v1, v2, v3 = v1*v1 + calc, (v1+v3) * v2, calc + v3 * v3
		if rec=='1': v1, v2, v3 = v1+v2, v1, v2
	return v2



	