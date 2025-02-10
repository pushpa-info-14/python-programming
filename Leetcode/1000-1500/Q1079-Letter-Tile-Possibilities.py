class Solution:
    def numTilePossibilities(self, tiles: str) -> int:

        res = [0]

        def dfs(tile_map):
            res[0] += 1
            for c in list(tile_map.keys()):
                tile_map[c] -= 1
                if tile_map[c] == 0:
                    del tile_map[c]

                dfs(tile_map)

                if c not in tile_map:
                    tile_map[c] = 0
                tile_map[c] += 1

        frequency = {}
        for c in tiles:
            if c not in frequency:
                frequency[c] = 0
            frequency[c] += 1

        dfs(frequency)
        return res[0] - 1


s = Solution()
print(s.numTilePossibilities("AAB"))
print(s.numTilePossibilities("AAABBC"))
print(s.numTilePossibilities("V"))
