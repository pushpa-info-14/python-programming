from typing import List


class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        ep = 1e-9

        def merge(a, b):
            yield a + b
            yield a - b
            yield b - a
            yield a * b
            if b != 0:
                yield a / b
            if a != 0:
                yield b / a

        def solve(nums):
            if len(nums) == 1:
                return abs(nums[0] - 24) < ep
            for i in range(len(nums) - 1):
                for j in range(i + 1, len(nums)):
                    a = nums[i]
                    b = nums[j]
                    new_nums = list(nums)
                    new_nums.remove(a)
                    new_nums.remove(b)
                    for new_value in merge(a, b):
                        if solve(sorted(new_nums + [new_value])):
                            return True
            return False

        return solve(sorted(cards))


s = Solution()
print(s.judgePoint24(cards=[4, 1, 8, 7]))
print(s.judgePoint24(cards=[1, 2, 1, 2]))
