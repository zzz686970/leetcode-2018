def maxDistToClosest(seats):
	seat_split = "".join(map(str, seats)).split('1')
	# print(seat_split)
	max_dist = max(map(len, seat_split))
	return max(len(seat_split[0]), len(seat_split[-1]), int(max_dist/2 + 0.5))

print(maxDistToClosest([1,0,0,0,1,0,1]))