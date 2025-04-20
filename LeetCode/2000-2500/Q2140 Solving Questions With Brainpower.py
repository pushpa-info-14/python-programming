from typing import List


class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        memo = [0] * n

        def backtrack(i):
            if i >= n:
                return 0
            if memo[i] != 0:
                return memo[i]
            points, brainpower = questions[i]
            res1 = backtrack(i + 1)  # Skip
            res2 = points + backtrack(i + brainpower + 1)  # Choose
            memo[i] = max(res1, res2)
            return memo[i]

        return backtrack(0)

    def mostPoints2(self, questions: List[List[int]]) -> int:
        n = len(questions)
        memo = [0] * n

        for i in reversed(range(n)):
            points, brainpower = questions[i]

            next_i = i + 1 + brainpower
            choose = points + (memo[next_i] if next_i < n else 0)
            skip = (memo[i + 1] if i + 1 < n else 0)
            memo[i] = max(choose, skip)

        return memo[0]


s = Solution()
print(s.mostPoints(questions=[[3, 2], [4, 3], [4, 4], [2, 5]]))
print(s.mostPoints(questions=[[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]]))
print(s.mostPoints2(questions=[[3, 2], [4, 3], [4, 4], [2, 5]]))
print(s.mostPoints2(questions=[[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]]))
