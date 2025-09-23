from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)

        candies1 = [1] * n
        candies2 = [1] * n

        for i in range(1, n):
            if ratings[i - 1] < ratings[i]:
                candies1[i] = candies1[i - 1] + 1
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candies2[i] = candies2[i + 1] + 1

        res = 0
        for i in range(n):
            res += max(candies1[i], candies2[i])

        return res

    def candy2(self, ratings: List[int]) -> int:
        n = len(ratings)
        left = [0] * n
        left[0] = 1
        for i in range(1, n):
            if ratings[i - 1] < ratings[i]:
                left[i] = left[i - 1] + 1
            else:
                left[i] = 1
        summation = max(1, left[-1])
        right = 1
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                cur = right + 1
            else:
                cur = 1
            right = cur
            summation += max(left[i], cur)

        return summation

    def candy3(self, ratings: List[int]) -> int:
        n = len(ratings)
        summation = 1
        i = 1

        while i < n:
            if ratings[i - 1] == ratings[i]:
                summation += 1
                i += 1
                continue
            peak = 1
            while i < n and ratings[i - 1] < ratings[i]:
                peak += 1
                summation += peak
                i += 1
            down = 1
            while i < n and ratings[i - 1] > ratings[i]:
                summation += down
                down += 1
                i += 1
            if down > peak:
                summation += down - peak
        return summation


s = Solution()
print(s.candy(ratings=[1, 0, 2]))
print(s.candy(ratings=[1, 2, 2]))
