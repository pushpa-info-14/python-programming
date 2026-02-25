from typing import List


class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        arr.sort()
        arr.sort(key=lambda x: x.bit_count())
        return arr


s = Solution()
print(s.sortByBits(arr=[0, 1, 2, 3, 4, 5, 6, 7, 8]))
print(s.sortByBits(arr=[1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]))
