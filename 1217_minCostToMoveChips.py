"""

for [1, 2, 3], would look like:

position 1	position 2	position 3
chip 1		chip 2		chip 3
for [2, 2, 2, 3, 3], would look like:

position 2	position 3
chip 1		chip 4
chip 2		chip 5
chip 3	
"""

def minCostToMoveChips(chips):

	odd_pos = sum(x % 2 for x in chips)
	return min(odd_pos, len(chips)-odd_pos)


def minCostToMoveChips(chips):
	even_parity = 0
    odd_parity = 0
    for chip in chips:
        if chip % 2 == 0:
            even_parity += 1
        else:
            odd_parity += 1
    return min(even_parity, odd_parity)