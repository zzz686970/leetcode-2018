def binaryGap(N):
	start = 0
	raw = bin(N)
	distance = []
	while True:
		pos = raw.find('1', start)
		if pos >= 0:
			distance.append(pos)
			start = pos + 1
			continue
		break

	if len(distance) == 1:
		return 0
	else:
		return max([distance[i+1] - distance[i]  for i in range(len(distance)-1)])

print(binaryGap(8))