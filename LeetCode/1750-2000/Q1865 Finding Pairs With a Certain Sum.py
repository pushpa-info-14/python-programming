from collections import Counter
from typing import List


class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1 = nums1
        self.nums2 = nums2
        self.freq = Counter(nums2)

    def add(self, index: int, val: int) -> None:
        before = self.nums2[index]
        self.nums2[index] = self.nums2[index] + val
        after = self.nums2[index]
        self.freq[before] -= 1
        self.freq[after] += 1

    def count(self, tot: int) -> int:
        res = 0
        for num in self.nums1:
            if tot - num in self.freq:
                res += self.freq[tot - num]
        return res


s = FindSumPairs([1, 1, 2, 2, 2, 3], [1, 4, 5, 2, 5, 4])
print(s.count(7))
s.add(3, 2)
print(s.count(8))
print(s.count(4))
s.add(0, 1)
s.add(1, 1)
print(s.count(7))
