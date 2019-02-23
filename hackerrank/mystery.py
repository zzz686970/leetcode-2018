a = 2437
b = 875

x, y = a, b 
while x != y:
	if x > y:
		x = x-y
	if x < y:
		y = y - x

	# print(x, y)

print(x, y )