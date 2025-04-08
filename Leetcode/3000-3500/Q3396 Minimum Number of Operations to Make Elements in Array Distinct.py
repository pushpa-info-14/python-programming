from collections import defaultdict
from typing import List


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        n = len(nums)
        freq = defaultdict(int)

        for num in nums:
            freq[num] += 1

        res = 0
        i = 0
        left = 0
        while i < n:
            if freq[nums[i]] > 1:
                res += 1
                for j in range(3):
                    if left + j < n:
                        freq[nums[left + j]] -= 1
                left += 3
                i = left
            else:
                i += 1
        return res

    def minimumOperations2(self, nums: List[int]) -> int:
        n = len(nums)
        seen = set()

        for i in reversed(range(n)):
            if nums[i] in seen:
                return i // 3 + 1
            else:
                seen.add(nums[i])
        return 0


s = Solution()
print(s.minimumOperations([1, 2, 3, 4, 2, 3, 3, 5, 7]))
print(s.minimumOperations([4, 5, 6, 4, 4]))
print(s.minimumOperations([6, 7, 8, 9]))
print(s.minimumOperations([5, 7, 11, 12, 12]))
print(s.minimumOperations2([1, 2, 3, 4, 2, 3, 3, 5, 7]))
print(s.minimumOperations2([4, 5, 6, 4, 4]))
print(s.minimumOperations2([6, 7, 8, 9]))
print(s.minimumOperations2([5, 7, 11, 12, 12]))
