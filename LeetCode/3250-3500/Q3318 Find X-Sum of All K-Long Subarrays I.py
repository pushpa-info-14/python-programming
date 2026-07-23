from collections import defaultdict
from typing import List


class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums)
        freq = defaultdict(int)
        res = []
        l = 0
        for r in range(n):
            freq[nums[r]] += 1
            while r - l + 1 > k:
                freq[nums[l]] -= 1
                if freq[nums[l]] == 0:
                    del freq[nums[l]]
                l += 1
            if r - l + 1 == k:
                pairs = []
                for key, value in freq.items():
                    pairs.append((value, key))
                pairs.sort(reverse=True)
                x_sum = 0
                for i in range(min(x, len(pairs))):
                    x_sum += pairs[i][0] * pairs[i][1]
                res.append(x_sum)
        return res


s = Solution()
print(s.findXSum(nums=[1, 1, 2, 2, 3, 4, 2, 3], k=6, x=2))
print(s.findXSum(nums=[3, 8, 7, 8, 7, 5], k=2, x=2))
print(s.findXSum(nums=[9, 2, 2], k=3, x=3))
