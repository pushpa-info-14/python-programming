from typing import List


class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        hBars.sort()
        vBars.sort()

        def get_streak(nums):
            max_streak = streak = 1
            for i in range(1, len(nums)):
                if nums[i - 1] + 1 == nums[i]:
                    streak += 1
                    max_streak = max(max_streak, streak)
                else:
                    streak = 1
            return max_streak

        width = min(get_streak(hBars), get_streak(vBars)) + 1
        return width * width


s = Solution()
print(s.maximizeSquareHoleArea(n=2, m=1, hBars=[2, 3], vBars=[2]))
print(s.maximizeSquareHoleArea(n=1, m=1, hBars=[2], vBars=[2]))
print(s.maximizeSquareHoleArea(n=2, m=3, hBars=[2, 3], vBars=[2, 4]))
