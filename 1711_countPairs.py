from typing import List 
from collections import Counter 

# class Solution:
#     def countPairs(self, deliciousness: List[int]) -> int:
#         mp = collections.Counter(deliciousness)
#         mp = collections.OrderedDict(sorted(mp.items(), key=lambda x: x[0]))
#         res = 0
#         MOD = 10 ** 9 + 7
#         isPower = lambda x: x & (x-1) == 0
#         for food in mp.keys():
#             if food: 
#                 if isPower(food): res += mp.get(0, 0)*mp[food] + mp[food] * (mp[food] - 1) // 2
#                 else:
#                     tar = 1 << (len(bin(food)) - 2)
#                     res += mp.get(tar-food, 0) * mp[food]
#             res %= MOD
#         return res


# def countPairs(deliciousness: List[int]) -> int:
#     pairs = [(k,v) for k,v in Counter(deliciousness).items()]
#     cnt = 0
#     for i in range(len(pairs)):
#         for j in range(len(pairs)):
#             temp = pairs[i][0] + pairs[j][0] 
#             while temp > 2:
#                 temp /= 2
            
#             if int(temp) == 2:
#                 if i == j:
#                     cnt += int((pairs[i][1] * (pairs[i][1] - 1)) / 2)
#                 else:
#                     cnt += pairs[i][1] * pairs[j][1]
    
#     return cnt % (10 ** 9 + 7)

def countPairs(deliciousness: List[int]) -> int:
    cnt = 0
    for i in range(len(deliciousness)-1):
        for j in range(i+1, len(deliciousness)):
            temp = deliciousness[i] + deliciousness[j]
            
            if temp != 0 and temp & (temp - 1) == 0:
                cnt += 1
    
    return cnt % (10 ** 9 + 7)    

if __name__ == '__main__':
    print(countPairs([149,107,1,63,0,1,6867,1325,5611,2581,39,89,46,18,12,20,22,234]))    
    print(countPairs([1,3,5,7,9]))    
    print(countPairs([2160,1936,3,29,27,5,2503,1593,2,0,16,0,3860,28908,6,2,15,49,6246,1946,23,105,7996,196,0,2,55,457,5,3,924,7268,16,48,4,0,12,116,2628,1468]))    