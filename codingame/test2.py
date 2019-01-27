## times
# def get_sec(time_str):
# 	h, m, s = time_str.split(':')
# 	return int(h) * 3600 + int(m) * 60 + int(s)

# print(get_sec('1:23:45'))
# print(get_sec('0:04:15'))
# print(get_sec('0:00:25'))

# timestamp.sort(key=lambda x: time.strptime(x, '%Y-%m-%d %H:%M:%S'))
# print(timestamp[0])

## lucky number
from sys import stderr
from time import process_time
from typing import Dict, List


def calculate_possibilities(max):
	"""Calculate the numbers of lucky numbers from 0 to 10**(max - 1)"""
	possibilities = { 0: 0, 1: 2 }
	index = 2
	while index < max:
		possibilities[index] = 2 * (9 ** (index - 1)) + 8 * possibilities[index - 1]
		index += 1
	return possibilities

def count(number):
	"""
	Count the lucky numbers from 0 to number with a fast mathematic range.
	"""
	digits = [int(c) for c in str(number)]
	pow_10: int = len(digits) - 1
	possibilities = calculate_possibilities(pow_10 + 1)
	lucky_numbers = 0

	found_lucky_digit = False
	lucky_digit = -1

	for digit in digits:
		if not found_lucky_digit:
			# We're in the classic case.
			if digit == 7:
				lucky_numbers += 6 * possibilities[pow_10] + 9 ** pow_10
			elif digit == 8:
				lucky_numbers += 7 * possibilities[pow_10] + 9 ** pow_10
			elif digit == 9:
				lucky_numbers += 7 * possibilities[pow_10] + 2 * (9 ** pow_10)
			else:
				lucky_numbers += digit * possibilities[pow_10]
		else:
			# Things change now that we know we have a lucky digit before us.
			if digit == 6:
				lucky_numbers += 6 * (9 ** pow_10)
				if found_lucky_digit and lucky_digit != 6:
					# We'll find no more lucky numbers.
					return lucky_numbers

			elif digit == 7:
				if lucky_digit == 6:
					lucky_numbers += 7 * (9 ** pow_10)
				else:
					lucky_numbers += 6 * (9 ** pow_10)

			elif digit == 8:
				lucky_numbers += 7 * (9 ** pow_10)
				if found_lucky_digit and lucky_digit != 8:
					# We'll find no more lucky numbers.
					lucky_numbers += 9 ** pow_10
					return lucky_numbers

			elif digit == 9:
				lucky_numbers += 8 * (9 ** pow_10)
			else:
				lucky_numbers += digit * (9 ** pow_10)

		pow_10 -= 1

		if not found_lucky_digit and (digit == 6 or digit == 8):
			lucky_digit = digit
			found_lucky_digit = True

	return lucky_numbers


l, r = 92871036442, 3363728910382456
start: float = process_time()

if l == r:
	## l and r is the same and only contain '6' or '8' but not the both
	if ('6' in str(l)) ^ ('8' in str(l)):
		print(1)
	else:
		print(0)
else:
	print(count(r+1) - count(l))
