from typing import List


class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        seen = set(nums)
        missing = k
        while missing in seen:
            missing += k
        return missing


s = Solution()
print(s.missingMultiple(nums=[8, 2, 3, 4, 6], k=2))
print(s.missingMultiple(nums=[1, 4, 7, 10, 15], k=5))
