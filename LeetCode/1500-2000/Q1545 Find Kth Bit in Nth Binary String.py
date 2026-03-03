from functools import cache


class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def invert(s):
            bits = []
            for c in s:
                if c == "1":
                    bits.append("0")
                else:
                    bits.append("1")
            return "".join(bits)

        @cache
        def dfs(x):
            if x == 1:
                return "0"
            return dfs(x - 1) + "1" + invert(dfs(x - 1))[::-1]

        sn = dfs(n)
        return sn[k - 1]

    def findKthBit2(self, n: int, k: int) -> str:
        if n == 1:
            return "0"
        mid = 1 << (n - 1)
        if k == mid:
            return "1"
        if k < mid:
            return self.findKthBit(n - 1, k)

        mirrored = (1 << n) - k
        bit = self.findKthBit(n - 1, mirrored)
        return "1" if bit == "0" else "0"


s = Solution()
print(s.findKthBit(n=3, k=1))
print(s.findKthBit(n=4, k=11))
print("-----------")
print(s.findKthBit2(n=3, k=1))
print(s.findKthBit2(n=4, k=11))
