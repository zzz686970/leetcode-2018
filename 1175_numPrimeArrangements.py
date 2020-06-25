from functools import reduce
import bisect 
import math 

def numPrimeArrangements(n):
    if n == 1: return 1
    prime_num = 0 
    for i in range(1, n+1):
        if i > 1:
            for j in range(2, i):
                if i % j == 0:
                    break
            else:
                prime_num += 1
    return reduce(lambda x, y: x*y, range(1, prime_num+1)) * reduce(lambda x, y: x*y, range(1, n - prime_num + 1)) % (10 ** 9 + 7)

def numPrimeArrangements(n):
    primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]
    cnt = bisect.bisect(primes, n)
    return math.factorial(cnt) * math.factorial(n - cnt) % (10 ** 9 + 7)

def numPrimeArrangements(n):
    prime = [True for _ in range(n+1)]
    p = 2
    while p * p <= n:
        if prime[p]:
            for i in range(p*p, n+1, p):
                prime[i] = False 
        p += 1
    primes = sum(prime[2:])
    return math.factorial(primes) * math.factorial(n - primes) % (10 ** 9 + 7)
    

if __name__ == '__main__':
    print(numPrimeArrangements(5))
    print(numPrimeArrangements(100))
    print(numPrimeArrangements(2))
    print(numPrimeArrangements(1))

