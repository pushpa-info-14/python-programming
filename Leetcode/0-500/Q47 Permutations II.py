from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        freq = {num: 0 for num in nums}
        for num in nums:
            freq[num] += 1

        def backtrack(cur):
            if len(cur) == n:
                res.append(cur.copy())
                return
            for num in freq:
                if freq[num] > 0:
                    freq[num] -= 1
                    cur.append(num)
                    backtrack(cur)
                    cur.pop()
                    freq[num] += 1

        backtrack([])
        return res


s = Solution()
print(s.permuteUnique([1, 1, 2]))
