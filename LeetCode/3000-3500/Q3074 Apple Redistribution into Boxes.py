from typing import List


class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        total = sum(apple)
        capacity.sort(reverse=True)
        res = 0
        for c in capacity:
            if total <= 0:
                break
            total -= c
            res += 1
        return res


s = Solution()
print(s.minimumBoxes(apple=[1, 3, 2], capacity=[4, 3, 1, 5, 2]))
print(s.minimumBoxes(apple=[5, 5, 5], capacity=[2, 4, 2, 7]))
