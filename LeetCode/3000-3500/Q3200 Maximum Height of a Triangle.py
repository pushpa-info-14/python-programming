class Solution:
    def maxHeightOfTriangle(self, red: int, blue: int) -> int:
        def solve(x, y):
            res = 0
            while x >= 0 and y >= 0:
                x -= res + 1
                if x >= 0:
                    res += 1
                else:
                    break
                y -= res + 1
                if y >= 0:
                    res += 1
                else:
                    break
            return res

        return max(solve(red, blue), solve(blue, red))


s = Solution()
print(s.maxHeightOfTriangle(red=2, blue=4))
print(s.maxHeightOfTriangle(red=2, blue=1))
print(s.maxHeightOfTriangle(red=1, blue=1))
print(s.maxHeightOfTriangle(red=10, blue=1))
