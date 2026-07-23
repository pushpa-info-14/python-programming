from collections import defaultdict
from typing import List


class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        freq = defaultdict(list)
        res = 0
        for i, num in enumerate(nums):
            if num not in freq:
                freq[num] = [i]
            else:
                for index in freq[num]:
                    if (index * i) % k == 0:
                        res += 1
                freq[num].append(i)
        return res


s = Solution()
print(s.countPairs(nums=[3, 1, 2, 2, 2, 1, 3], k=2))
print(s.countPairs(nums=[1, 2, 3, 4], k=1))
