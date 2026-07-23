from typing import List


class Solution:
    def minTime(self, skill: List[int], mana: List[int]) -> int:
        n, m = len(skill), len(mana)
        total_skill = sum(skill)
        gap = 0
        for i in range(0, m - 1):
            b = mana[i]
            delta = mana[i + 1] - b
            mx = 0
            pref = 0
            for a in skill:
                need = (a * b) - (pref * delta)
                if need > mx:
                    mx = need
                pref += a
            gap += mx
        return gap + total_skill * mana[-1]

    def minTime2(self, skill: List[int], mana: List[int]) -> int:
        n, m = len(skill), len(mana)
        f = [0] * n
        for x in mana:
            now = 0
            for i in range(n):
                now = max(now, f[i]) + skill[i] * x
            f[n - 1] = now
            for i in range(n - 2, -1, -1):
                f[i] = f[i + 1] - skill[i + 1] * x
        return f[n - 1]


s = Solution()
print(s.minTime(skill=[1, 5, 2, 4], mana=[5, 1, 4, 2]))
print(s.minTime(skill=[1, 1, 1], mana=[1, 1, 1]))
print(s.minTime(skill=[1, 2, 3, 4], mana=[1, 2]))
print(s.minTime2(skill=[1, 5, 2, 4], mana=[5, 1, 4, 2]))
print(s.minTime2(skill=[1, 1, 1], mana=[1, 1, 1]))
print(s.minTime2(skill=[1, 2, 3, 4], mana=[1, 2]))
