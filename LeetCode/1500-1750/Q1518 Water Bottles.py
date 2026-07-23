class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        res = 0
        empty = 0
        while numBottles > 0:
            res += numBottles
            temp = (empty + numBottles) // numExchange
            empty = (empty + numBottles) % numExchange
            numBottles = temp
        return res


s = Solution()
print(s.numWaterBottles(numBottles=9, numExchange=3))
print(s.numWaterBottles(numBottles=15, numExchange=4))
print(s.numWaterBottles(numBottles=12, numExchange=4))
