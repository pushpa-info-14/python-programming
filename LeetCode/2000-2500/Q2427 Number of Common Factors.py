def factors(x):
    res = []
    i = 1
    while i <= x:
        if x % i == 0:
            res.append(i)
        i += 1

    return res


class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        f1 = factors(a)
        f2 = factors(b)
        seen = set(f1)
        res = 0
        for x in f2:
            if x in seen:
                res += 1
        return res


s = Solution()
print(s.commonFactors(a=12, b=6))
print(s.commonFactors(a=25, b=30))
