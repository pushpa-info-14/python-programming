from typing import List


class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        mod = 10 ** 9 + 7
        hFences.extend([1, m])
        vFences.extend([1, n])
        hFences.sort()
        vFences.sort()

        h_candidates = set()
        for i in range(len(hFences)):
            for j in range(i + 1, len(hFences)):
                h_candidates.add(hFences[j] - hFences[i])
        v_candidates = set()
        for i in range(len(vFences)):
            for j in range(i + 1, len(vFences)):
                v_candidates.add(vFences[j] - vFences[i])

        width = 0
        for x in h_candidates:
            if x in v_candidates:
                width = max(width, x)
        return width * width % mod if width != 0 else -1


s = Solution()
print(s.maximizeSquareArea(m=4, n=3, hFences=[2, 3], vFences=[2]))
print(s.maximizeSquareArea(m=6, n=7, hFences=[2], vFences=[4]))
