from collections import Counter
from typing import List


class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        counter = Counter(arr)
        for x in arr:
            if x == 0:
                if counter[x] > 1:
                    return True
            elif 2 * x in counter:
                return True
        return False


s = Solution()
print(s.checkIfExist(arr=[10, 2, 5, 3]))
print(s.checkIfExist(arr=[3, 1, 7, 11]))
