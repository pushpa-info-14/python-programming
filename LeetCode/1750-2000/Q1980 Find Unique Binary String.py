from functools import cache
from typing import List


class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        nums_set = set(nums)
        res = ""

        @cache
        def dfs(cur):
            nonlocal res
            if len(cur) == n:
                if cur in nums_set:
                    return False
                res = cur
                return True
            if dfs(cur + "0") or dfs(cur + "1"):
                return True
            return False

        dfs("")
        return res


s = Solution()
print(s.findDifferentBinaryString(["01", "10"]))
print(s.findDifferentBinaryString(["00", "01"]))
print(s.findDifferentBinaryString(["111", "011", "001"]))
