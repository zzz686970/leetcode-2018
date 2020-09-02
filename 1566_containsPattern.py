from typing import List 

## O((n-mk)(mk)) time and O(mk) space
def containsPattern(arr: List[int], m: int, k: int) -> bool:
    for i in range(len(arr) - m*k + 1):
        if arr[i:i+m] * k == arr[i: i + m*k] :
            return True
    return False

## O(n) time, O(1) space
def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
    streak = 0
    for i in range(len(arr)-m):
        streak = streak + 1 if arr[i] == arr[i+m] else 0
        if streak == (k-1)*m: return True
    return False


if __name__ == '__main__':
	print(containsPattern(arr = [1,2,4,4,4,4], m = 1, k = 3))
	print(containsPattern(arr = [1,2,1,2,1,1,1,3], m = 2, k = 2))
	print(containsPattern(arr = [1,2,1,2,1,3], m = 2, k = 3))
	print(containsPattern(arr = [1,2,3,1,2], m = 2, k = 2))
	print(containsPattern(arr = [2,2,2,2], m = 2, k = 3))
