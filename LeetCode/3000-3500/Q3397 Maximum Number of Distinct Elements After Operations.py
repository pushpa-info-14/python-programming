from typing import List


class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        nums.sort()
        seen = set()
        last = nums[0] - k
        for num in nums:
            last = max(last, num - k)
            for new_num in range(last, num + k + 1):
                if new_num not in seen:
                    seen.add(new_num)
                    last = new_num
                    break
        return len(seen)


s = Solution()
print(s.maxDistinctElements(nums=[1, 2, 2, 3, 3, 4], k=2))
print(s.maxDistinctElements(nums=[4, 4, 4, 4], k=1))
print(s.maxDistinctElements(nums=[56,56,54,54], k=0))
