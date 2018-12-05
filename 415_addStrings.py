def addStrings(num1, num2):
	carry, ans = 0, []

	a = [i for i in num1]
	b = [j for j in num2]
	while len(a) or len(b):
		num1 = ord(a.pop())-ord('0') if len(a) else 0
		num2 = ord(b.pop()) - ord('0') if len(b) else 0
		temp = num1 + num2 + carry
		ans.append(str(temp%10))
		carry = temp // 10
    ## 所有运算结束还有进位
	if carry: ans.append(str(carry))
	return "".join(ans)[::-1]


print(addStrings('123','12'))