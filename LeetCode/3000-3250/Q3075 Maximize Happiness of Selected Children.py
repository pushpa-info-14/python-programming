from typing import List


class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)
        index = 0
        cur = 0
        res = 0
        for i in range(k):
            res += max(0, happiness[index] - cur)
            index += 1
            cur += 1
        return res


s = Solution()
print(s.maximumHappinessSum(happiness=[1, 2, 3], k=2))  # 4
print(s.maximumHappinessSum(happiness=[1, 1, 1, 1], k=2))  # 1
print(s.maximumHappinessSum(happiness=[2, 3, 4, 5], k=1))  # 5
