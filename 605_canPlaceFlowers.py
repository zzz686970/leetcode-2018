def canPlaceFlowers(flowerbed, n):
	# result = dict()
	# cnt = n
	# if len(flowerbed) == 1 and flowerbed[0] == 0:
	# 	cnt -= 1
	# elif flowerbed[0]== 0 and flowerbed[1]==0:
	# 	cnt -= 1
	# elif flowerbed[-1]==0 and flowerbed[-2]==0:
	# 	cnt -= 1

	# else:
	# 	for index in range(1, len(flowerbed)-1):
	# 		if index+1 <= len(flowerbed) and flowerbed[index-1] == 0 and flowerbed[index+1] == 0 and flowerbed[index]== 0:
	# 			flowerbed[index] = 1
	# 			cnt -= 1
	# 	if cnt == 0: 
	# 		return True

	# return False
	for i, x in enumerate(flowerbed):
		if (not x and (i==0 or flowerbed[i-1]==0) and (i==len(flowerbed)-1 or flowerbed[i+1]==0)):
			n -= 1
			flowerbed[i] = 1

	return n <= 0

flowerbed=[0,0,1,0,1]
n= 1
print(canPlaceFlowers(flowerbed, n))


