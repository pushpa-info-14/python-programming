from collections import defaultdict
from typing import List


class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        unique_count = 0
        unique_elements = set()
        for num in nums:
            if num not in unique_elements:
                unique_elements.add(num)
                unique_count += 1

        n = len(nums)
        freq = defaultdict(int)
        l, r = 0, 0
        res = 0
        while r < n:
            freq[nums[r]] += 1

            while len(freq.keys()) == unique_count:
                res += n - r
                freq[nums[l]] -= 1
                if freq[nums[l]] == 0:
                    del freq[nums[l]]
                l += 1
            r += 1
        return res


s = Solution()
print(s.countCompleteSubarrays([1, 3, 1, 2, 2]))
print(s.countCompleteSubarrays([5, 5, 5, 5]))
