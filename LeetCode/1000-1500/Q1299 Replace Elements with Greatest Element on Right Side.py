from typing import List


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        max_num = -1
        for i in reversed(range(n)):
            cur = max(max_num, arr[i])
            arr[i] = max_num
            max_num = cur
        return arr


s = Solution()
print(s.replaceElements(arr=[17, 18, 5, 4, 6, 1]))
print(s.replaceElements(arr=[400]))
