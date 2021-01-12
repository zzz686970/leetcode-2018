from typing import List
class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
    	src, dst = zip(*edges)
        return list(set(src) - set(dst))
        # return list(set(a) - set(b) for a, b in edges)
        
        # return list(set(range(n)) - set(e[1] for e in edges))
#         source = set()
#         dest = set()
#         for src, dst in edges:
#             dest.add(dst)
#             if src in dest:
#                 if src in source:
#                     source.remove(src)
#                 else:
#                     continue
#             elif src not in source:
#                 source.add(src)
        
#         return list(source.difference(dest))


a = [[1,2],[3,4]]

i, j = zip(*a)
print(set(i) - set(j))