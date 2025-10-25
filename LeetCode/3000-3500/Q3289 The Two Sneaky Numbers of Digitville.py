from typing import List


class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        seen = set()
        res = []
        for num in nums:
            if num not in seen:
                seen.add(num)
            else:
                res.append(num)
                if len(res) == 2:
                    break
        return res


s = Solution()
print(s.getSneakyNumbers(nums=[0, 1, 1, 0]))
print(s.getSneakyNumbers(nums=[0, 3, 2, 1, 3, 2]))
print(s.getSneakyNumbers(nums=[7, 1, 5, 4, 3, 4, 6, 0, 9, 5, 8, 2]))
