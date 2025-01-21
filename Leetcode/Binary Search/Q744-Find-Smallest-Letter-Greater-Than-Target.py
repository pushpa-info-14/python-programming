from typing import List


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        l, r = 0, len(letters)
        while l < r:
            mid = (l + r) // 2
            if letters[mid] <= target:
                l = mid + 1
            else:
                r = mid
        if r == len(letters):
            return letters[0]
        return letters[r]


s = Solution()
print(s.nextGreatestLetter(["c", "f", "j"], "a"))  # c
print(s.nextGreatestLetter(["c", "f", "j"], "c"))  # f
print(s.nextGreatestLetter(["x", "x", "y", "y"], "z"))  # x
