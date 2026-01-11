from collections import defaultdict
from typing import List


class Solution:
    def maximumSum(self, nums: List[int]) -> int:

        def sum_of_digits(number):
            summation = 0
            while number:
                summation += number % 10
                number = number // 10
            return summation

        res = -1
        frequency = defaultdict(int)
        previous_max_num = defaultdict(int)
        for i in range(len(nums)):
            cur = sum_of_digits(nums[i])

            if frequency[cur] > 0:
                num1 = previous_max_num[cur]
                num2 = nums[i]
                res = max(res, num1 + num2)
            previous_max_num[cur] = max(previous_max_num[cur], nums[i])
            frequency[cur] += 1
        return res

    def maximumSum2(self, nums: List[int]) -> int:

        def sum_of_digits(number):
            summation = 0
            while number:
                summation += number % 10
                number = number // 10
            return summation

        res = -1
        previous_max = defaultdict(int)
        for i in range(len(nums)):
            cur = sum_of_digits(nums[i])

            if previous_max[cur] > 0:
                num1 = previous_max[cur]
                num2 = nums[i]
                res = max(res, num1 + num2)
            previous_max[cur] = max(previous_max[cur], nums[i])
        return res


s = Solution()
print(s.maximumSum([18, 43, 36, 13, 7]))
print(s.maximumSum([10, 12, 19, 14]))
print(s.maximumSum([41, 23, 32, 14]))

print(s.maximumSum2([18, 43, 36, 13, 7]))
print(s.maximumSum2([10, 12, 19, 14]))
print(s.maximumSum2([41, 23, 32, 14]))
