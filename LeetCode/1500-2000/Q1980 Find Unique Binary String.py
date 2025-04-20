from typing import List


class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        nums_set = set(nums)
        res = [""]

        def backtrack(cur):
            if len(cur) == n:
                if cur in nums_set:
                    return False
                res[0] = cur
                return True
            if backtrack(cur + "0") or backtrack(cur + "1"):
                return True
            return False

        backtrack("")
        return res[0]


s = Solution()
print(s.findDifferentBinaryString(["01", "10"]))
print(s.findDifferentBinaryString(["00", "01"]))
print(s.findDifferentBinaryString(["111", "011", "001"]))
