def calPoints(ops):
	each_round = ['x' for i in range(len(ops))]
	# print(each_round)
	last_round = []
	for i, el in enumerate(ops):
		
		if el.isdigit() or (el.startswith('-') and el[1:].isdigit()):
			each_round[i] = int(el)
			last_round.append(int(ops[i]))

		elif el == 'C':
			# each_round[i-1]  = 'x'
			## double check the position

			for k in range(len(each_round[:i]), 0, -1):
				if each_round[k-1] != 'x':
					each_round[k-1]  = 'x'
				else:
					continue
				break
			last_round.pop()


		elif el == 'D':
			each_round[i] = last_round[-1] * 2
			last_round.append(each_round[i])

		elif el == '+':

			# second_last = 'x'
			# # print(each_round[:i])

			# for k in range(len(each_round[:i-1]), 0, -1):
			# 	if each_round[k-1] != 'x':
			# 		second_last = int(each_round[k-1])
			# 	else:
			# 		continue
			# 	break

			# each_round[i] = second_last + last_round[-1]
			each_round[i] = last_round[-2] + last_round[-1]
			last_round.append(each_round[i])

		print(i, last_round, each_round)

	return sum(el for el in each_round if el !='x')

ops = ["5","2","C","D","+"]
ops2 = ["5","-2","4","C","D","9","+","+"]
ops3 = ["-60","D","-36","30","13","C","C","-33","53","79"]
ops4 = ["1","C","-62","-45","-68"]
ops5 = ["36","28","70","65","C","+","33","-46","84","C"]
print(calPoints(ops4))

