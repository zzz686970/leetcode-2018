def numberOfLines(widths, S):
	import string, math
	group = dict(zip(string.ascii_letters[:26], widths))
	line_length, line = 0, 1
	for char in S:
		line_length += group.get(char)
		if line_length > 100:
			line += 1
			line_length = group.get(char)

	return [line, line_length ]


# widths = [4,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
# S = "bbbcccdddaaa"

widths = [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
S = "abcdefghijklmnopqrstuvwxyz"
print(numberOfLines(widths, S))