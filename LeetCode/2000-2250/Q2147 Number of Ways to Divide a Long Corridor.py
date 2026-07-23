class Solution:
    def numberOfWays(self, corridor: str) -> int:
        mod = 10 ** 9 + 7
        seats = corridor.count('S')
        if seats == 0 or seats & 1:
            return 0
        counter = {'S': 0, 'P': 0}
        res = 1
        for c in corridor:
            counter[c] += 1
            if c == 'S' and counter['S'] == 2:
                counter['P'] = 0
            if counter['S'] == 3:
                counter['S'] = 1
                res = res * (counter['P'] + 1)
        return res % mod


s = Solution()
print(s.numberOfWays(corridor="SSPPSPS"))
print(s.numberOfWays(corridor="PPSPSP"))
print(s.numberOfWays(corridor="S"))
