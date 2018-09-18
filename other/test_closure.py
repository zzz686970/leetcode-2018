def maker(N):
	def action(X):
		return X ** N
	return action

f = maker(2)
print(f(3))


def f():
	a = []
	for i in range(5):
		a.append(lambda x, i=i: i ** x)
	return a

t = f()

print(t[1](2),t[2](2))

def tester(start):
	state=start
	def nested(label):
		nonlocal state 
		print(label, start)
		state += 1
	return nested

f = tester(3)
print(f(2))