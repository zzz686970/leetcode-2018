"""
rand7，让你实现rand5
"""
import random
def rand7():
	return random.randint(1, 7)

def rand5():
	res = 6
	while res > 5:
		res = rand7()

	return res 

## 概率，P(x=1) = 1/7 + (2/7) * 1/7 + ...
## 如果第一次没有生成1，那么第二次则是在第一次生成5～6的基础上

"""如何生成随机数
给定能随机生成整数1到5的函数，写出能随机生成整数1到7的函数
需要保证等概率生成，那么构建的规则是
a > b, Randa2 = a * (Randa - 1) + Randa 表示1... a2随机数
如果仍然a2 < b, 继续 Randa3 = a * (Randa2 -1 ) + Randa
直到ak > b
""" 
class solution2()
	def rand5(self):
		return random.randint(1, 5)

	def rand7(self):
		res = 25
		while res > 21:
			res = 5 * (rand5() -1 ) + rand5()
 
		return res % 7 + 1

if __name__ == '__main__':
	d = {i:0 for i in range(1, 8)}
	for i in range(1, 1000001):
		d[rand7()] += 1
	for i in range(1, 8):
		print(i, '出现的概率是：', float(d[i] / 1000000))

