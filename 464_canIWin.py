class Solution:
	def canIWin(self, maxChoosableInteger, desiredTotal):
		total = maxChoosableInteger * (maxChoosableInteger + 1) // 2
		if maxChoosableInteger >= desiredTotal:
			return True

		if total < desiredTotal:
			return False
		elif total == desiredTotal:
			return (maxChoosableInteger %2 == 1)

		bit_mast = 1 << maxChoosableInteger

		cnt = 0
		for i in range(maxChoosableInteger):
			cnt += i
			if cnt > desiredTotal:
				return False

		return True

	def checkWin(self, max_num, bit_mask, remain_sum)

print(canIWin(18, 79))

