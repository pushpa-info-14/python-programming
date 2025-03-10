from typing import List


class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        l_sum = 0
        r_sum = 0

        for i in range(k):
            l_sum += cardPoints[i]
        max_sum = l_sum

        r = n - 1
        for i in reversed(range(k)):
            l_sum -= cardPoints[i]
            r_sum += cardPoints[r]
            r -= 1
            max_sum = max(max_sum, l_sum + r_sum)
        return max_sum


s = Solution()
print(s.maxScore([6, 2, 3, 4, 7, 2, 1, 7, 1], 4))
