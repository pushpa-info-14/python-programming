from typing import List


class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        res = set()
        cur = {0}
        for n in arr:
            cur = {x | n for x in cur}
            cur.add(n)
            res |= cur
        return len(res)


s = Solution()
print(s.subarrayBitwiseORs(arr=[0]))
print(s.subarrayBitwiseORs(arr=[1, 1, 2]))
print(s.subarrayBitwiseORs(arr=[1, 2, 4]))
