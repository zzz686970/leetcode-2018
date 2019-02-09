# def mySqrt(x):
# 	# return int(x ** 0.5)

# 	## binary search
# 	start = 0
# 	end = x
# 	while end > start:
# 		mid = start + (end-start) // 2
# 		if mid ** 2 == x: 
# 			return mid
# 		elif mid ** 2 > x:
# 			end = mid - 1
# 		else:
# 			if (mid+1) ** 2 > x:
# 				return mid
# 			else:
# 				start = mid + 1
# 	return start

## newton method
"""[summary]
Slope of the tangent line is f'(Xn)
f(Xn) - 0 = f'(Xn) * (Xn-Xn+1)
Xn+1 = Xn - f(Xn) / f'(Xn)

f(x) = x^2 - n
f'(x) = 2 * x
Xn+1 = Xn - (Xn - n/Xn) / 2
Xn+1 = (Xn + n/Xn) / 2

Xn+1 = Xn - (Xn ^ k - a) / k Xn ^ (k-1) = Xn(k-1)/k  + a/(k * (Xn ^(k-1)))
Keyword Arguments:
"""

def mySqrt(n):
	res = n 
	while abs(res ** 2 - n) > 0.0000001:
		res = (res + n/res ) / 2

	return res 

print(mySqrt(8))