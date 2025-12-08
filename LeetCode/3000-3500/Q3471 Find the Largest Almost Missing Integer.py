from collections import Counter
from typing import List


class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        n = len(nums)
        counter = Counter(nums)
        if k == 1:
            for x in sorted(counter.keys(), reverse=True):
                if counter[x] == 1:
                    return x
            return -1
        if k == n:
            return max(nums)
        candidates = []
        if counter[nums[0]] == 1:
            candidates.append(nums[0])
        if counter[nums[-1]] == 1:
            candidates.append(nums[-1])
        candidates.sort(reverse=True)

        if candidates:
            return candidates[0]
        return -1


s = Solution()
print(s.largestInteger(nums=[3, 9, 2, 1, 7], k=3))
print(s.largestInteger(nums=[3, 9, 7, 2, 1, 7], k=4))
print(s.largestInteger(nums=[0, 0], k=1))
print(s.largestInteger(nums=[0, 0], k=2))
