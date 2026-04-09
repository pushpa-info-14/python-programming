from collections import defaultdict
from typing import List


class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        mod = 10 ** 9 + 7
        n = len(nums)
        sq = int(n ** 0.5)
        mp = defaultdict(list)
        for l, r, k, v in queries:
            if k > sq:
                for i in range(l, r + 1, k):
                    nums[i] = (nums[i] * v) % mod
            else:
                mp[k].append((l, r, v))

        for k in mp:
            diff = [1] * (n + k)
            for l, r, v in mp[k]:
                diff[l] = (diff[l] * v) % mod
                r_plus1 = l + ((r - l) // k + 1) * k  # 1 + items * size of each step
                diff[r_plus1] = (diff[r_plus1] * pow(v, -1, mod)) % mod

            for i in range(k, n):
                diff[i] = (diff[i] * diff[i - k]) % mod

            for i in range(n):
                nums[i] = (diff[i] * nums[i]) % mod

        res = 0
        for num in nums:
            res ^= num
        return res


s = Solution()
print(s.xorAfterQueries(nums=[1, 1, 1], queries=[[0, 2, 1, 4]]))
print(s.xorAfterQueries(nums=[2, 3, 1, 5, 4], queries=[[1, 4, 2, 3], [0, 2, 1, 2]]))
