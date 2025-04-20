from collections import defaultdict
from math import ceil
from typing import List


class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        freq = defaultdict(int)
        for answer in answers:
            freq[answer] += 1
        res = 0
        for key, count in freq.items():
            group_size = key + 1
            num_groups = ceil(count / group_size)
            # num_groups = (count + key) // group_size
            res += num_groups * group_size
        return res


s = Solution()
print(s.numRabbits([1, 1, 2]))
print(s.numRabbits([10, 10, 10]))
print(s.numRabbits([1, 0, 1, 0, 0]))
