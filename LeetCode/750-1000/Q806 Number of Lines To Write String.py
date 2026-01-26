from typing import List


class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        line = 1
        cur = 0
        for c in s:
            width = widths[ord(c) - ord('a')]
            if cur + width <= 100:
                cur += width
            else:
                line += 1
                cur = width
        return [line, cur]


s = Solution()
print(s.numberOfLines(
    widths=[10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
    s="abcdefghijklmnopqrstuvwxyz"))
print(s.numberOfLines(
    widths=[4, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
    s="bbbcccdddaaa"))
