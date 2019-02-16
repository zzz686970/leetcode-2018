"""一筐鸡蛋：
1个1个拿，正好拿完
2个2个拿，还剩1个
3个3个拿，正好拿完
4个4个拿，还剩1个
5个5个拿，还差1个
6个6个拿，还剩3个
7个7个拿，正好拿完
8个8个拿，还剩1个
9个9个拿，正好拿完
问筐里最少有多少鸡蛋

[description]
""" 

def solution():

	y = 1

	while True:
		if y % 2 == y % 4 == y % 8 and y % 3 == y % 9 == 0 and y % 7 ==0 and y % 5 == 4 and y % 6 == 3:
			return y 

		y += 1

print(solution())

## 1449