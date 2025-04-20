from typing import List


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        missing = []
        l = 1
        for i in arr:
            if l < i:
                while l < i:
                    missing.append(l)
                    l += 1

            l = i + 1

        if len(missing) < k:
            return arr[-1] + (k - len(missing))

        return missing[k - 1]


s = Solution()
print(s.findKthPositive([2, 3, 4, 7, 11], 5))
print(s.findKthPositive([1, 2, 3, 4], 2))
