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

    def getSneakyNumbers2(self, nums: List[int]) -> List[int]:
        n = len(nums) - 2
        xor = 0
        for x in range(n):
            xor ^= x
        for x in nums:
            xor ^= x
        diff_bit = xor & -xor
        xor1 = 0
        xor2 = 0
        for x in range(n):
            if x & diff_bit:
                xor1 ^= x
            else:
                xor2 ^= x
        for x in nums:
            if x & diff_bit:
                xor1 ^= x
            else:
                xor2 ^= x

        return [xor1, xor2]


s = Solution()
print(s.getSneakyNumbers(nums=[0, 1, 1, 0]))
print(s.getSneakyNumbers(nums=[0, 3, 2, 1, 3, 2]))
print(s.getSneakyNumbers(nums=[7, 1, 5, 4, 3, 4, 6, 0, 9, 5, 8, 2]))
print(s.getSneakyNumbers2(nums=[0, 1, 1, 0]))
print(s.getSneakyNumbers2(nums=[0, 3, 2, 1, 3, 2]))
print(s.getSneakyNumbers2(nums=[7, 1, 5, 4, 3, 4, 6, 0, 9, 5, 8, 2]))
