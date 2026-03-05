from typing import List


class Solution:
    def checkEqualPartitions(self, nums: List[int], target: int) -> bool:
        product = 1
        for num in nums:
            product *= num
            if target % num != 0:
                return False

        if product == target ** 2:
            return True
        return False


s = Solution()
print(s.checkEqualPartitions(nums=[3, 1, 6, 8, 4], target=24))
print(s.checkEqualPartitions(nums=[2, 5, 3, 7], target=15))
print(s.checkEqualPartitions(nums=[21, 7, 12, 6, 24, 9], target=1512))
print(s.checkEqualPartitions(nums=[11, 22, 5, 10], target=110))
print(s.checkEqualPartitions(nums=[24, 3, 8, 9], target=72))
