from typing import List


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        s = set()

        for num in nums:
            if num not in s:
                s.add(num)

        sorted_list = sorted(s, reverse=True)
        if len(sorted_list) < 3:
            return sorted_list[0]
        return sorted_list[2]


s = Solution()
print(s.thirdMax([3, 2, 1]))
print(s.thirdMax([1, 2]))
print(s.thirdMax([2, 2, 3, 1]))
