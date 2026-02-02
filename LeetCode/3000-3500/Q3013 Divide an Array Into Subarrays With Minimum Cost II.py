from typing import List

from sortedcontainers import SortedList


class Solution:
    def minimumCost(self, nums: List[int], k: int, dist: int) -> int:
        n = len(nums)
        small, large = SortedList(), SortedList()

        # Initial window
        for i in range(1, dist + 2):
            small.add((nums[i], i))
        while len(small) >= k:
            large.add(small.pop())
        curr = sum(v for v, _ in small)
        res = curr

        for i in range(dist + 2, n):
            l_key = (nums[i - dist - 1], i - dist - 1)
            r_key = (nums[i], i)

            # Remove left
            if l_key in small:
                small.discard(l_key)
                curr -= nums[i - dist - 1]
                if large:
                    l = large.pop(0)
                    small.add(l)
                    curr += l[0]
            elif l_key in large:
                large.discard(l_key)

            # Add right
            small.add(r_key)
            curr += nums[i]

            if len(small) >= k:
                s = small.pop()
                large.add(s)
                curr -= s[0]
            res = min(res, curr)
        return res + nums[0]


solution = Solution()
print(solution.minimumCost(nums=[1, 3, 2, 6, 4, 2], k=3, dist=3))
print(solution.minimumCost(nums=[10, 1, 2, 2, 2, 1], k=4, dist=3))
print(solution.minimumCost(nums=[10, 8, 18, 9], k=3, dist=1))
