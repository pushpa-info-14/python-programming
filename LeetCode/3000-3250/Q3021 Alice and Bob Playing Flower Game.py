class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        odd_lane1 = (n + 1) // 2
        even_lane2 = m // 2
        even_lane1 = n // 2
        odd_lane2 = (m + 1) // 2
        return odd_lane1 * even_lane2 + even_lane1 * odd_lane2


s = Solution()
print(s.flowerGame(n=3, m=2))
print(s.flowerGame(n=1, m=1))
