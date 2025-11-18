from typing import List


class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        n = len(bits)
        if n == 1 or bits[-2] == 0:
            return True

        cur = 0
        last = -1
        while cur < n:
            if bits[cur] == 0:
                last = 1
                cur += 1
            else:
                last = 2
                cur += 2
        return last == 1


s = Solution()
print(s.isOneBitCharacter(bits=[1, 0, 0]))
print(s.isOneBitCharacter(bits=[1, 1, 1, 0]))
