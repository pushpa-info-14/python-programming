from typing import List


class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        nums_set = set(nums)
        res = 0
        for num in nums:
            if num + diff in nums_set and num + 2 * diff in nums_set:
                res += 1
        return res


s = Solution()
print(s.arithmeticTriplets(nums=[0, 1, 4, 6, 7, 10], diff=3))
print(s.arithmeticTriplets(nums=[4, 5, 6, 7, 8, 9], diff=2))
