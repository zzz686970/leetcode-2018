def biggerIsGreater(w):
    s = ''
    i = len(w)-1
    while i >=0 :

        if i>0 and  w[i] > w[i-1] :
            s += w[i-1]
            s += w[i]
            i -= 1
            break
        i -= 1
        s += w[i]
    print(i)
    s += w[:i][::-1]
    
    return 'no answer' if s == "".join(reversed(s)) else "".join(reversed(s))


if __name__ == '__main__':
	# print(biggerIsGreater('ab'))
	# print(biggerIsGreater('bb'))
	# print(biggerIsGreater('hefg'))
	# print(biggerIsGreater('dhck'))
	print(biggerIsGreater('dkhc'))
	## hcdk