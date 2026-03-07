class Solution:
    def minFlips(self, s: str) -> int:
        w = len(s)
        s += s
        n = len(s)

        def solve(target):
            cur = 0
            expected = ["0"] * n
            for i in range(w):
                if s[i] != target:
                    cur += 1
                expected[i] = target
                target = "1" if target == "0" else "0"
            res = cur
            for i in range(w, n):
                if s[i - w] != expected[i - w]:
                    cur -= 1
                if s[i] != target:
                    cur += 1
                res = min(res, cur)
                target = "1" if target == "0" else "0"
            return res

        return min(solve("0"), solve("1"))


s = Solution()
print(s.minFlips(s="111000"))
print(s.minFlips(s="010"))
print(s.minFlips(s="1110"))
