def intToRoman(num):
	letters=['I','V','X','L','C','D','M']
	values = [1,5,10,50,100,500,1000]
	ans = {}
	for a, b in zip(letters, values):
		ans[a] = b

	

	print(ans)

print(intToRoman(1))