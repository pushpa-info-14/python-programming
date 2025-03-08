import math


class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        n = len(blocks)
        w = 0
        min_w = math.inf
        l, r = 0, 0
        while r < n:
            if blocks[r] == "W":
                w += 1
            if r - l + 1 == k:
                min_w = min(min_w, w)
                if blocks[l] == "W":
                    w -= 1
                l += 1
            r += 1

        return min_w


s = Solution()
print(s.minimumRecolors("WBBWWBBWBW", 7))  # 3
print(s.minimumRecolors("WBWBBBW", 2))  # 0
