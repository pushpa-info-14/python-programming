from typing import List


class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        res = 0
        for i in range(n):
            curr = 0
            for j in range(i, n):
                curr += nums[j] == target
                res += curr * 2 > j - i + 1
        return res


s = Solution()
print(s.countMajoritySubarrays(nums=[1, 2, 2, 3], target=2))
print(s.countMajoritySubarrays(nums=[1, 1, 1, 1], target=1))
print(s.countMajoritySubarrays(nums=[1, 2, 3], target=4))
