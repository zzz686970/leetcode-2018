def mirrorReflection(p, q):
	## 横坐标为p的倍数，这样最终才能到达一个点
	k = 1
	while p * k % q: k += 1

	## 横坐标为x的偶数倍，反射在下面
	if k % 2 == 0: return 0
	else:
		## 横坐标和p的关系，若为p的偶数倍，则反射到2
		r = p * k // q 
		if r % 2: return 1
		else: return 2