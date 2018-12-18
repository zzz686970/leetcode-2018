"""Fib

Some ways to compute fibs

def fibs(n):
	fibs = [0, 1]
	for in in range(2, n+1):
		fibs.append(fibs[-1] + fibs[-2])

	return fibs

## save computed value in a dict to prevent re-compute
def fib(n, computed={0:0,1:1}):
	if n not in computed:
		computed[n] = fib(n-1, computed) + fib(n-2, computed)
	return computed[n]

## decorator
import functools
@functools.lru_cache(None)
def fibs(n):
	if n < 2:
		return n
	return fibs(n-1) + fibs(n-2)

## count up
def fibs(n):
	a, b = 0, 1
	for _ in range(n):
		a, b = b, a+b
	return n

## bit ops
def fib(n):
	v1, v2, v3 = 1,1,0
	for rec in bin(n)[3:]:
		calc = v1 * v2
		v1, v2, v3 = v1*v2 + calc, (v1+v3) * v2, calc + v3 * v3
		if rec=='1': v1, v2, v3 = v1+v2, v1, v2
	return v2


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

benchmark test:
def benchmark(n, *args):
    print("-" * 80)
    for func in args:
        print(func.__name__)
        start = clock()
        try:
            ret = func(n)
            #print("Result:", ret)
        except RuntimeError as e:
            print("Error:", e)
        print("Time:", "{:.8f}".format(clock() - start))
        print()

benchmark(500, fib_iter, fib_memo, fib_local, fib_local_exc, fib_lru)

"""


def climbStairs(n):
	## time exceed
	# if n == 1: return 1
	# if n == 2: return 2
	# return self.climbStairs(n-1) + self.climbStairs(n-2)

	## way 2
	a, b = 1, 2
	for i in range(1, n):
		a, b = b, a+b
	return a 

assert 1 == climbStairs(1)
assert 3 == climbStairs(3)


