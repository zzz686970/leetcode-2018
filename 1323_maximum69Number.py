def maximum69Number(num):
	ans = list(map(str, str(num)))
	for i in range(len(ans)):
		if ans[i] == '6':
			ans[i] = '9'
			break

	return int("".join(ans))

if __name__ == '__main__':
	print(maximum69Number(9669))
	print(maximum69Number(9996))
	print(maximum69Number(9999))
