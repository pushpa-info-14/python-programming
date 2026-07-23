class Solution:
    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:
        mp = {
            "a": 1,
            "b": 2,
            "c": 3,
            "d": 4,
            "e": 5,
            "f": 6,
            "g": 7,
            "h": 8
        }

        r1, c1 = mp[coordinate1[0]] % 2, int(coordinate1[1]) % 2
        r2, c2 = mp[coordinate2[0]] % 2, int(coordinate2[1]) % 2
        if r1 == r2:
            return c1 == c2
        else:
            return abs(c1 - c2) == 1


s = Solution()
print(s.checkTwoChessboards(coordinate1="a1", coordinate2="c3"))
print(s.checkTwoChessboards(coordinate1="a1", coordinate2="h3"))
print(s.checkTwoChessboards(coordinate1="h7", coordinate2="c8"))
