from typing import List


class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        target.sort()
        arr.sort()
        for i in range(len(target)):
            if target[i] != arr[i]:
                return False
        return True


s = Solution()
print(s.canBeEqual(target=[1, 2, 3, 4], arr=[2, 4, 1, 3]))
print(s.canBeEqual(target=[7], arr=[7]))
print(s.canBeEqual(target=[3, 7, 9], arr=[3, 7, 11]))
