from math import log
from typing import List


class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        val = k - 1
        steps = 0

        while val > 0:
            jump = int(log(val, 2))
            lower = 1 << jump
            if operations[jump]:
                steps += 1
            val -= lower
        return chr(97 + (steps % 26))

    def kthCharacter2(self, k: int, operations: List[int]) -> str:
        def solve(n):
            if n == 1:
                return 0
            if n.bit_count() == 1:
                return operations[n.bit_length() - 2] + solve(n // 2)

            msb_v = 1 << (n.bit_length() - 1)
            pred = n - msb_v

            op_index = n.bit_length() - 1
            return operations[op_index] + solve(pred)

        shifts = solve(k)

        shifts %= 26

        return chr(ord("a") + shifts)


s = Solution()
print(s.kthCharacter(k=5, operations=[0, 0, 0]))
print(s.kthCharacter(k=10, operations=[0, 1, 0, 1]))
print(s.kthCharacter2(k=5, operations=[0, 0, 0]))
print(s.kthCharacter2(k=10, operations=[0, 1, 0, 1]))
