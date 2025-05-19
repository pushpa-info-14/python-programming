from collections import defaultdict
from typing import List


class Solution:
    def triangleType(self, nums: List[int]) -> str:
        triangle_type = {
            1: "equilateral",
            2: "isosceles",
            3: "scalene"
        }

        a, b, c = nums[0], nums[1], nums[2]
        if a + b > c and a + c > b and b + c > a:
            freq = defaultdict(int)
            for num in nums:
                freq[num] += 1

            return triangle_type[len(freq.keys())]
        return "none"


s = Solution()
print(s.triangleType(nums=[3, 3, 3]))
print(s.triangleType(nums=[3, 4, 5]))
print(s.triangleType(nums=[3, 2, 1]))
