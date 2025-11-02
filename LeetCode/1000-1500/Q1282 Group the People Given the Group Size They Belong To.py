from collections import defaultdict
from typing import List


class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        mp = defaultdict(list)
        res = []
        for i in range(len(groupSizes)):
            mp[groupSizes[i]].append(i)
        for key in mp.keys():
            people = mp[key]
            for i in range(0, len(people), key):
                res.append(people[i:i + key])
        return res

    def groupThePeople2(self, groupSizes: List[int]) -> List[List[int]]:
        group = {}
        res = []
        for i in range(len(groupSizes)):
            size = groupSizes[i]
            if size not in group:
                group[size] = []
            group[size].append(i)

            if len(group[size]) == size:
                res.append(group[size])
                group[size] = []
        return res


s = Solution()
print(s.groupThePeople(groupSizes=[3, 3, 3, 3, 3, 1, 3]))
print(s.groupThePeople(groupSizes=[2, 1, 3, 3, 3, 2]))
print(s.groupThePeople2(groupSizes=[3, 3, 3, 3, 3, 1, 3]))
print(s.groupThePeople2(groupSizes=[2, 1, 3, 3, 3, 2]))
