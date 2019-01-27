# import sys
# inputs = []
# for line in sys.stdin:
# 	# inputs.append(line.strip())
# 	sys.stdout.write(line)

# # ans = []
# # if len(inputs) <= 1: print(0)
# # else:
# # 	content = result[1].split(' ')
# # 	min_diff = abs(int(content[0]))
# # 	for temp in content:
# # 		if abs(int(temp)) <= min_diff:
# # 			abs.append(int(temp))

# # 	compare = min([abs(el) for el in abs])
# # 	print(max(el for el in ans if el==compare))

cnt = 0
l, h = (600, 199)
lists = [str(i) for i in range(l, h+1)]
for num in lists:
	if all(el in num for el in ('6', '8')):
		continue
	elif '6' in num:
		print(num)
		cnt += 1
	elif '8' in num:
		cnt += 1
		print(num)
	else:
		continue
print(cnt)
# cnt2= 0
# for i in range(100, 199):
# 	if '8' in str(i):
# 		cnt2 += 1
# print(cnt2)