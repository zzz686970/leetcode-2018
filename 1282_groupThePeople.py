class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        dic = collections.defaultdict(list)
        for i, val in enumerate(groupSizes):
            dic[val].append(i)
        
        # return [li[i:i+s] for s, li in dic.items() for i in range(0, len(li), s)]
        return [list(subgroup) for size, group in dic.items() for subgroup in zip(*[iter(group)]*size)]
