class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        ds = "NSEW"
        counts = [0] * 4
        res = 0

        for c in s:
            d = ds.index(c)
            counts[d] += 1

            max_x = max(counts[0], counts[1])
            min_x = min(counts[0], counts[1])

            ck = k
            used = min(min_x, ck)
            min_x -= used
            ck -= used
            max_x += used

            max_y = max(counts[2], counts[3])
            min_y = min(counts[2], counts[3])

            used = min(min_y, ck)
            min_y -= used
            ck -= used
            max_y += used

            res = max(res, max_x - min_x + max_y - min_y)
        return res


s = Solution()
print(s.maxDistance(s="NWSE", k=1))
print(s.maxDistance(s="NSWWEW", k=3))
print(s.maxDistance(s="WEES", k=2))
