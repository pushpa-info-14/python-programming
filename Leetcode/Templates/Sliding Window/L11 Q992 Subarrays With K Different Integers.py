from typing import List


class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:

        def subarraysWithLessThanKDistinct(k):
            n = len(nums)
            freq = {}
            l, r = 0, 0
            res = 0

            while r < n:
                if nums[r] not in freq:
                    freq[nums[r]] = 0
                freq[nums[r]] += 1

                while len(freq) > k:
                    freq[nums[l]] -= 1
                    if freq[nums[l]] == 0:
                        del freq[nums[l]]
                    l += 1

                res += r - l + 1
                r += 1
            return res

        return subarraysWithLessThanKDistinct(k) - subarraysWithLessThanKDistinct(k - 1)


s = Solution()
print(s.subarraysWithKDistinct([1, 2, 1, 2, 3], 2))
print(s.subarraysWithKDistinct([1, 2, 1, 3, 4], 3))
