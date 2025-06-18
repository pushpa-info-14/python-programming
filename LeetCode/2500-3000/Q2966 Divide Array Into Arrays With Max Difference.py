from typing import List


class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []
        for i in range(0, n, 3):
            if nums[i + 2] - nums[i] > k:
                return []
            else:
                res.append([nums[i], nums[i + 1], nums[i + 2]])
        return res


s = Solution()
print(s.divideArray(nums=[1, 3, 4, 8, 7, 9, 3, 5, 1], k=2))
print(s.divideArray(nums=[2, 4, 2, 2, 5, 2], k=2))
print(s.divideArray(nums=[4, 2, 9, 8, 2, 12, 7, 12, 10, 5, 8, 5, 5, 7, 9, 2, 5, 11], k=14))
