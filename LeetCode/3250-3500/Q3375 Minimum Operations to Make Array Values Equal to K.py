from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        seen = set()
        for num in nums:
            if num < k:
                return -1
            elif num > k:
                seen.add(num)
        return len(seen)

    def minOperations2(self, nums: List[int], k: int) -> int:
        if min(nums) < k:
            return -1
        elif k in nums:
            return len(set(nums)) - 1
        else:
            return len(set(nums))


s = Solution()
print(s.minOperations(nums=[5, 2, 5, 4, 5], k=2))
print(s.minOperations(nums=[2, 1, 2], k=2))
print(s.minOperations(nums=[9, 7, 5, 3], k=1))
print(s.minOperations2(nums=[5, 2, 5, 4, 5], k=2))
print(s.minOperations2(nums=[2, 1, 2], k=2))
print(s.minOperations2(nums=[9, 7, 5, 3], k=1))
