from typing import List


class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        freq = {}

        for num in nums:
            if num not in freq:
                freq[num] = 0
            freq[num] += 1

        for cnt in freq.values():
            if cnt % 2:
                return False
        return True


s = Solution()
print(s.divideArray([3, 2, 3, 2, 2, 2]))
print(s.divideArray([1, 2, 3, 4]))
