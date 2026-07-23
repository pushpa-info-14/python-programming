from typing import List


class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        res = []
        counter = [0] * (n + 1)
        cur = 0
        for a, b in zip(A, B):
            counter[a] += 1
            counter[b] += 1
            if counter[a] == 2:
                cur += 1
            if a != b:
                if counter[b] == 2:
                    cur += 1
            res.append(cur)
        return res


s = Solution()
print(s.findThePrefixCommonArray(A=[1, 3, 2, 4], B=[3, 1, 2, 4]))
print(s.findThePrefixCommonArray(A=[2, 3, 1], B=[3, 1, 2]))
