def powerfulIntegers(x, y, bound):
	xs = [x**i for i in range(20) if x **i < bound]
	ys = [y**i for i in range(20) if y **i < bound]

	return list({i+j for i in xs for j in ys if i+j <= bound})
