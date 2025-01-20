from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        result = [0]
        shift = 1

        for i in range(1, n + 1):
            if i == shift * 2:
                shift = shift * 2
            result.append(1 + result[i - shift])
        return result


s = Solution()
print(s.countBits(2))
print(s.countBits(5))
