def solution(n):
	"""
		 x         
		  x        
		 o x       
		  o x      
		 x o x     
		  x o x    
		 o x o x   
		  o x o x  
		 x o x o x 
x o x o x x o x o x
 x o x o x
  x o x o
   x o x o
	x o x
	 x o x
	  x o
	   x o
		x
		 x

  x  
   x 
x o x
 x
  x



	  x
	 x
	o x
	 o x
x o x o x
 x o
  x o
   x
	x
	"""
	# n = int(input())
	longest = []
	ans = []
	if n % 2:
		longest = ['x' if (i+1)% 2 else 'o' for i in range(n) ]
	else:
		
		longest = ['x' if (i+1)% 2 else 'o' for i in range(n//2) ] * 2


	for i in range(n):
		if i == 0:
			ans.append(" ".join(longest))
		else:
			tmp = longest[:(n//2+1 - int(i/2+0.5))]
			ans.append(" "*i + " ".join(tmp) + (2*n-1-i -len(" ".join(tmp))) * " ")


	left = [el[::-1] for el in ans[1:]][::-1]
	for x in left + ans:
		print(x)

	# return ans

for i in [3,5,10]:
	print("*********************\nNumber: %d" %(i)) 
	solution(i)
	print("*********************\n")
