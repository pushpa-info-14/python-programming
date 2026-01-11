import bisect
from collections import Counter, defaultdict
from typing import List


class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        freq = Counter(nums)
        range_freq = defaultdict(int)
        for num in nums:
            range_freq[num - k] += 1
            range_freq[num] -= 1
            range_freq[num + 1] += 1
            range_freq[num + k + 1] -= 1
        cur = 0
        res = 0
        for k in sorted(range_freq.keys()):
            cur += range_freq[k]
            res = max(res, freq[k] + min(numOperations, cur))
        return res

    def maxFrequency2(self, nums: List[int], k: int, numOperations: int) -> int:
        n = len(nums)
        nums.sort()
        res = 0
        l, r = 0, 0
        freq = Counter(nums)

        for i in nums:
            while r < n and nums[r] <= i + k:
                r += 1
            while nums[l] < i - k:
                l += 1
            curr = min(r - l, freq[i] + numOperations)
            res = max(res, curr)

        l = 0
        for r in range(n):
            while nums[l] < nums[r] - (2 * k):
                l += 1
            res = max(res, min(r - l + 1, numOperations))
        return res

    def maxFrequency3(self, nums: List[int], k: int, numOperations: int) -> int:
        res = 0
        freq = Counter(nums)
        nums.sort()
        for num in nums:
            for x in [num, num + k, num - k]:
                left = bisect.bisect_left(nums, x - k)
                right = bisect.bisect_right(nums, x + k)
                count = right - left
                res = max(res, freq[x] + min(numOperations, count - freq[x]))
        return res


s = Solution()
print(s.maxFrequency(nums=[1, 4, 5], k=1, numOperations=2))  # 2
print(s.maxFrequency(nums=[5, 11, 20, 20], k=5, numOperations=1))  # 2
print(s.maxFrequency(nums=[5, 11, 20, 20, 20, 20], k=5, numOperations=1))  # 4
print(s.maxFrequency(nums=[5, 11, 20, 20, 20, 20], k=5, numOperations=4))  # 4
print(s.maxFrequency(nums=[88, 53], k=27, numOperations=2))  # 2
print(s.maxFrequency(nums=[1, 90], k=76, numOperations=1))  # 1
print(s.maxFrequency(nums=[23, 54], k=77, numOperations=1))  # 2
print(s.maxFrequency(nums=[37, 30, 37], k=26, numOperations=1))  # 3
print(s.maxFrequency2(nums=[1, 4, 5], k=1, numOperations=2))  # 2
print(s.maxFrequency2(nums=[5, 11, 20, 20], k=5, numOperations=1))  # 2
print(s.maxFrequency2(nums=[5, 11, 20, 20, 20, 20], k=5, numOperations=1))  # 4
print(s.maxFrequency2(nums=[5, 11, 20, 20, 20, 20], k=5, numOperations=4))  # 4
print(s.maxFrequency2(nums=[88, 53], k=27, numOperations=2))  # 2
print(s.maxFrequency2(nums=[1, 90], k=76, numOperations=1))  # 1
print(s.maxFrequency2(nums=[23, 54], k=77, numOperations=1))  # 2
print(s.maxFrequency2(nums=[37, 30, 37], k=26, numOperations=1))  # 3
print(s.maxFrequency3(nums=[1, 4, 5], k=1, numOperations=2))  # 2
print(s.maxFrequency3(nums=[5, 11, 20, 20], k=5, numOperations=1))  # 2
print(s.maxFrequency3(nums=[5, 11, 20, 20, 20, 20], k=5, numOperations=1))  # 4
print(s.maxFrequency3(nums=[5, 11, 20, 20, 20, 20], k=5, numOperations=4))  # 4
print(s.maxFrequency3(nums=[88, 53], k=27, numOperations=2))  # 2
print(s.maxFrequency3(nums=[1, 90], k=76, numOperations=1))  # 1
print(s.maxFrequency3(nums=[23, 54], k=77, numOperations=1))  # 2
print(s.maxFrequency3(nums=[37, 30, 37], k=26, numOperations=1))  # 3
