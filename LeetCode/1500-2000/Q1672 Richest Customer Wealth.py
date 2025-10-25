from typing import List


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        res = 0
        for account in accounts:
            cur = 0
            for amount in account:
                cur += amount
            res = max(res, cur)
        return res


s = Solution()
print(s.maximumWealth(accounts=[[1, 2, 3], [3, 2, 1]]))
print(s.maximumWealth(accounts=[[1, 5], [7, 3], [3, 5]]))
print(s.maximumWealth(accounts=[[2, 8, 7], [7, 1, 3], [1, 9, 5]]))
