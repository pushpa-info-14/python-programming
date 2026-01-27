from typing import List


class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        if n & 1:
            res += nums[n // 2]
        i = 0
        j = n - 1
        while i < j:
            if i != j:
                x = nums[i]
                digits = []
                y = nums[j]
                while y:
                    digits.append(y % 10)
                    y //= 10
                for digit in digits[::-1]:
                    x = x * 10 + digit
                res += x
            i += 1
            j -= 1
        return res

    def findTheArrayConcVal2(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        if n & 1:
            res += nums[n // 2]
        i = 0
        j = n - 1
        while i < j:
            if i != j:
                res += int(str(nums[i]) + str(nums[j]))
            i += 1
            j -= 1
        return res


s = Solution()
print(s.findTheArrayConcVal(nums=[7, 52, 2, 4]))
print(s.findTheArrayConcVal(nums=[5, 14, 13, 8, 12]))
print("-----------------")
print(s.findTheArrayConcVal2(nums=[7, 52, 2, 4]))
print(s.findTheArrayConcVal2(nums=[5, 14, 13, 8, 12]))
