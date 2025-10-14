from typing import List


class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        for i in range(n - 2 * k + 1):
            is_found = True
            cur = i
            for j in range(i + k, min(i + 2 * k - 1, n - 1)):
                if nums[cur] >= nums[cur + 1] or nums[j] >= nums[j + 1]:
                    is_found = False
                    break
                cur += 1
            if is_found:
                return True
        return False


s = Solution()
print(s.hasIncreasingSubarrays(nums=[2, 5, 7, 8, 9, 2, 3, 4, 3, 1], k=3))
print(s.hasIncreasingSubarrays(nums=[1, 2, 3, 4, 4, 4, 4, 5, 6, 7], k=5))
print(s.hasIncreasingSubarrays(nums=[-15, 19], k=1))
