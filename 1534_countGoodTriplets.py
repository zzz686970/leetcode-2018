def countGoodTriplets(arr, a, b, c):
    ans = 0 
    for i in range(len(arr)-2):
        for j in range(i+1, len(arr)-1):
            if abs(arr[i] - arr[j]) > a: continue 
            for k in range(j+1, len(arr)):
                if abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
                    ans += 1

    return ans 

if __name__ == '__main__':
    print(countGoodTriplets(arr = [3,0,1,1,9,7], a = 7, b = 2, c = 3))
    print(countGoodTriplets(arr = [1,1,2,2,3], a = 0, b = 0, c = 1))