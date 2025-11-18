from typing import List


class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        res = []
        for num in nums:
            if num < 10:
                res.append(num)
            else:
                cur = []
                while num:
                    cur.append(num % 10)
                    num //= 10
                res += cur[::-1]
        return res


s = Solution()
print(s.separateDigits(nums=[13, 25, 83, 77]))
print(s.separateDigits(nums=[7, 1, 3, 9]))
