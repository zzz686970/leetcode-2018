class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
    	## accumulate 
        for i in range(len(arr) -1 ):
            arr[i+1] ^= arr[i]
        
        return [arr[l-1] ^ arr[r] if l else arr[r] for l, r in queries]

        