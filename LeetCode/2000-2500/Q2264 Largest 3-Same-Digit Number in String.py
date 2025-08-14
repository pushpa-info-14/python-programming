from collections import defaultdict


class Solution:
    def largestGoodInteger(self, num: str) -> str:
        n = len(num)
        if n < 3:
            return ""

        freq = defaultdict(int)
        res = ""
        l = 0
        for r in range(n):
            while r - l + 1 > 3:
                freq[num[l]] -= 1
                if not freq[num[l]]:
                    del freq[num[l]]
                l += 1
            freq[num[r]] += 1
            if r - l + 1 == 3 and len(freq.keys()) == 1:
                res = max(res, num[l: r + 1])

        return res

    def largestGoodInteger2(self, num: str) -> str:
        n = len(num)
        if n < 3:
            return ""
        res = ""
        prev = ""
        count = 0
        for cur in num:
            if cur == prev:
                count += 1
            else:
                count = 1
            if count == 3:
                res = max(res, cur * 3)
                count = 1
            prev = cur
        return res


s = Solution()
print(s.largestGoodInteger(num="6777133339"))
print(s.largestGoodInteger(num="2300019"))
print(s.largestGoodInteger(num="42352338"))
print(s.largestGoodInteger2(num="6777133339"))
print(s.largestGoodInteger2(num="2300019"))
print(s.largestGoodInteger2(num="42352338"))
