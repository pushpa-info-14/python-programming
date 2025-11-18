from collections import Counter
from typing import List


class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        counter = Counter(nums)
        temp = []
        for num, freq in counter.items():
            temp.append([freq, num])
        temp.sort(key=lambda x: (x[0], -x[1]))
        res = []
        for freq, num in temp:
            for i in range(freq):
                res.append(num)
        return res


s = Solution()
print(s.frequencySort(nums=[1, 1, 2, 2, 2, 3]))
print(s.frequencySort(nums=[2, 3, 1, 3, 2]))
print(s.frequencySort(nums=[-1, 1, -6, 4, 5, -6, 1, 4, 1]))
