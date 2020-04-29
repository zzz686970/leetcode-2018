from collections import defaultdict
# Time complexity O(n^2)

for i in range(4):
    f"a_{i}" = i 

print(a_1)

def delete_nth_naive(array, n):
    ans = []
    for num in array:
        if ans.count(num) < n:
            ans.append(num)
    return ans

# Time Complexity O(n), using hash tables.
def delete_nth(array,n):
    result = []
    counts = defaultdict(int)

    for i in array:
        if counts[i] < n:
            result.append(i)
            counts[i] += 1
    return result


x = [1,2,3,1,2,1,2,3]
print(delete_nth(x, n=2))
print(delete_nth_naive(x, n=2))