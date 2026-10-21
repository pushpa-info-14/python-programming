from typing import List


class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums)
        sor = sorted([i for i in range(n)], key=lambda i: (sum(int(c) for c in str(nums[i])), nums[i]))
        g = {sor[i]: i for i in range(n)}

        visited = [False] * n
        cycles = 0
        for i in range(n):
            if visited[i]:
                continue

            cur = i
            while not visited[cur]:
                visited[cur] = True
                cur = g[cur]
            cycles += 1
        return n - cycles


s = Solution()
print(s.minSwaps(nums=[37, 100]))
print(s.minSwaps(nums=[22, 14, 33, 7]))
print(s.minSwaps(nums=[18, 43, 34, 16]))
