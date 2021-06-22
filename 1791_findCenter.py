def findCenter(self, e: List[List[int]]) -> int:
	return (set(e[0]) & set(e[1])).pop()

def findCenter(self, e: List[List[int]]) -> int:
	if e[0][0]==e[1][0] or e[0][0]==e[1][1]:
		return e[0][0]
	return e[0][1]

# def findCenter(self, e: List[List[int]]) -> int:
# 	return e[0][e[0][1] in e[1]]

def findCenter(self, e: List[List[int]]) -> int:
    return max(e[0], key=e[1].count)

def findCenter(self, e: List[List[int]]) -> int:
    return mode(e[0] + e[1])    	