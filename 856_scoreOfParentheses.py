def scoreOfParentheses(S):
	stack = [0]
	for c in S:
		if c == '(':
			stack.append(0)
		else:
			num = stack.pop()
			stack[-1] += (1 if num==0 else 2 * num)

	return stack[0]

print(scoreOfParentheses('(())'))
