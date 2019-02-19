"""[summary]

Description

We want to calculate a sum of squares of some integers, excepting negatives
The first line of the input will be an integer N (1 <= N <= 100)
Each of the following N test cases consists of one line containing an integer X (0 < X <= 100), followed by X integers (Yn, -100 <= Yn <= 100) space-separated on the next line
For each test case, calculate the sum of squares of the integers excepting negatives, and print the calculated sum to the output. No blank line between test cases
(Take input from standard input, and output to standard output)
Rules

Write it in Go Programming Language
Your source code must be a single file (package main)
Do not use for statement
You may only use standard library packages
Sample Input

2
4
3 -1 1 14
5
9 6 -53 32 16
Sample Output

206
1397
""" 
import sys

filter_func = lambda x: x > 0
square_func = lambda x: x ** 2

## use recursive to compute

def get_number_n():
	try:
		N = int(input())
		if N < 1 or N > 100:
			print("Input should be within [1, 100]")
			sys.exit(1)
	except ValueError:
		print("Not a valid integer")
		sys.exit(1)

	return N

def get_result(N):
	try:
		X = int(input())
		if X < 1 or X > 100:
			raise ValueError

		Y = map(int, input().split())
		result = sum(map(square_func, filter(filter_func, Y)))
		print(result)
	except ValueError:
		print("Wrong input for test case")

	return get_result(N-1)


if __name__ == '__main__':
	N = get_number_n()
	get_result(N)






















