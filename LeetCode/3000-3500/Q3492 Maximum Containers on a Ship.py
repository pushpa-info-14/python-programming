class Solution:
    def maxContainers(self, n: int, w: int, maxWeight: int) -> int:
        cells = n * n
        total_weight = cells * w
        if total_weight <= maxWeight:
            return cells
        else:
            return maxWeight // w


s = Solution()
print(s.maxContainers(n=2, w=3, maxWeight=15))
print(s.maxContainers(n=3, w=5, maxWeight=20))
