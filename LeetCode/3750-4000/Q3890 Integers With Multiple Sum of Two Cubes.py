from collections import defaultdict


class Solution:
    def findGoodIntegers(self, n: int) -> list[int]:
        mp = defaultdict(int)
        for a in range(1000):
            for b in range(a, 1000):
                x = a ** 3 + b ** 3
                if x > n:
                    break
                mp[x] += 1
        res = []
        for x in mp.keys():
            if mp[x] > 1:
                res.append(x)
        res.sort()
        return res


s = Solution()
print(s.findGoodIntegers(4104))
print(s.findGoodIntegers(578))
print(s.findGoodIntegers(972241))
