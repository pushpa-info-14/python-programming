from collections import deque
from typing import List

from sortedcontainers import SortedList


class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        n = len(nums)
        mod = 10 ** 9 + 7
        dp = [0] * (n + 1)
        prefix = [0] * (n + 1)
        window = SortedList()
        dp[0] = 1
        prefix[0] = 1
        l = 0
        for r in range(n):
            window.add(nums[r])
            while l <= r and window[-1] - window[0] > k:
                window.remove(nums[l])
                l += 1
            dp[r + 1] = (prefix[r] - (prefix[l - 1] if l > 0 else 0)) % mod
            prefix[r + 1] = (prefix[r] + dp[r + 1]) % mod

        return dp[n]

    def countPartitions2(self, nums: List[int], k: int) -> int:
        n = len(nums)
        mod = 10 ** 9 + 7
        dp = [0] * (n + 1)
        prefix = [0] * (n + 1)
        min_q = deque()
        max_q = deque()
        dp[0] = 1
        prefix[0] = 1
        l = 0
        for r in range(n):
            # maintain the maximum value queue
            while max_q and nums[max_q[-1]] <= nums[r]:
                max_q.pop()
            max_q.append(r)

            # maintain the minimum value queue
            while min_q and nums[min_q[-1]] >= nums[r]:
                min_q.pop()
            min_q.append(r)

            # adjust window
            while max_q and min_q and nums[max_q[0]] - nums[min_q[0]] > k:
                if max_q[0] == l:
                    max_q.popleft()
                if min_q[0] == l:
                    min_q.popleft()
                l += 1

            if l > 0:
                dp[r + 1] = (prefix[r] - prefix[l - 1] + mod) % mod
            else:
                dp[r + 1] = prefix[r] % mod
            prefix[r + 1] = (prefix[r] + dp[r + 1]) % mod

        return dp[n]


s = Solution()
print(s.countPartitions(nums=[9, 4, 1, 3, 7], k=4))
print(s.countPartitions(nums=[3, 3, 4], k=0))
print(s.countPartitions2(nums=[9, 4, 1, 3, 7], k=4))
print(s.countPartitions2(nums=[3, 3, 4], k=0))
