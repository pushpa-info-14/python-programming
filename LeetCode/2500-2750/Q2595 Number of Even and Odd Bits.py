from typing import List


class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        odd = 0
        even = 0
        is_odd = False
        while n:
            if is_odd:
                odd += n & 1
            else:
                even += n & 1
            n >>= 1
            is_odd = not is_odd

        return [even, odd]


s = Solution()
print(s.evenOddBit(50))
print(s.evenOddBit(2))
