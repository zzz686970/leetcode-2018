import collections 
import string 

def sortString(s):
    bucket = collections.Counter(s)
    flag = True 
    ans = ''
    while bucket:
        for el in sorted(bucket) if flag else reversed(sorted(bucket)):
            ans += el
            bucket[el] -= 1

            if bucket[el] == 0:
                del bucket[el]

        flag = not flag 

    return ans 

def sortString(s):
    bucket = collections.Counter(s)
    flag = True 
    ans = ''
    while len(ans) < len(s):
        for i in range(26):
            c = string.ascii_lowercase[i if flag else ~i]
            if bucket[c] > 0:
                ans += c 
                bucket[c] -= 1

        flag = not flag 

    return ans 

if __name__ == '__main__':
    print(sortString(s = "aaaabbbbcccc"))
