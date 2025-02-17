from collections import defaultdict


class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        count = defaultdict(int)
        for c in tiles:
            count[c] += 1

        def dfs():
            res = 0
            for c in count:
                if count[c] > 0:
                    count[c] -= 1
                    res += 1
                    res += dfs()
                    count[c] += 1
            return res
        return dfs()


s = Solution()
print(s.numTilePossibilities("AAB"))
print(s.numTilePossibilities("AAABBC"))
print(s.numTilePossibilities("V"))
