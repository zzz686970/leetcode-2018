def replaceElements(arr):
	## initial last element
	mx = -1
	for i in range(len(arr)-1, -1, -1):
		arr[i], mx = mx, max(mx, arr[i])

	return arr 

if __name__ == '__main__':
	print(replaceElements(arr = [17,18,5,4,6,1]))