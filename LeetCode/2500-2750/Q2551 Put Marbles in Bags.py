from typing import List


class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        if k == 1:
            return 0
        n = len(weights)
        splits = []
        for i in range(n - 1):
            splits.append(weights[i] + weights[i + 1])

        splits.sort()
        i = k - 1
        max_score = sum(splits[-i:])
        min_score = sum(splits[:i])
        return max_score - min_score


s = Solution()
print(s.putMarbles(weights=[1, 3, 5, 1], k=2))
print(s.putMarbles(weights=[1, 3], k=2))
