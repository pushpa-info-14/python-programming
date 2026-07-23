from collections import defaultdict
from typing import List


class Solution:
    def getDistances(self, arr: List[int]) -> List[int]:
        n = len(arr)
        mp = defaultdict(list)
        for i in range(n):
            mp[arr[i]].append(i)
        for num in mp.keys():
            size = len(mp[num])
            cur = mp[num]
            pfx_sum = [0] * (size + 1)
            for i in range(1, size + 1):
                pfx_sum[i] = cur[i - 1] + pfx_sum[i - 1]
            for i in range(size):
                arr[cur[i]] = i * cur[i] - pfx_sum[i] + pfx_sum[-1] - pfx_sum[i + 1] - (size - i - 1) * cur[i]
        return arr


s = Solution()
print(s.getDistances(arr=[2, 1, 3, 1, 2, 3, 3]))
print(s.getDistances(arr=[10, 5, 10, 10]))
