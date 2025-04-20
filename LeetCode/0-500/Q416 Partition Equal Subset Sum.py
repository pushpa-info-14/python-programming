from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        summation = sum(nums)
        if summation % 2:
            return False

        target = summation // 2
        dp = set()
        dp.add(0)
        for i in reversed(range(len(nums))):
            for t in dp.copy():
                if t + nums[i] == target:
                    return True
                dp.add(t + nums[i])
        return False


s = Solution()
print(s.canPartition([1, 5, 11, 5]))
print(s.canPartition([1, 2, 3, 5]))
