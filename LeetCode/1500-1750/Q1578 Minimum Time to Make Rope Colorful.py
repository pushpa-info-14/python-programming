from typing import List


class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        n = len(colors)
        res = 0
        i = 0
        total, maxi = 0, 0
        while i < n:
            while i + 1 < n and colors[i] == colors[i + 1]:
                total += neededTime[i]
                maxi = max(maxi, neededTime[i])
                i += 1
            if total:
                total += neededTime[i]
                maxi = max(maxi, neededTime[i])
                res += total - maxi
                total = 0
                maxi = 0
            i += 1
        return res


s = Solution()
print(s.minCost(colors="abaac", neededTime=[1, 2, 3, 4, 5]))
print(s.minCost(colors="abc", neededTime=[1, 2, 3]))
print(s.minCost(colors="aabaa", neededTime=[1, 2, 3, 4, 1]))
print(s.minCost(colors="bbbaaa", neededTime=[4, 9, 3, 8, 8, 9]))
