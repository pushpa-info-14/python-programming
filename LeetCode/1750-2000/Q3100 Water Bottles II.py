class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        b_drunk = 0
        b_full = numBottles
        b_empty = 0
        while b_full > 0:
            b_drunk += b_full
            b_empty += b_full
            b_full = 0
            if b_empty >= numExchange:
                b_full += 1
                b_empty -= numExchange
                numExchange += 1
        return b_drunk

    def maxBottlesDrunk2(self, numBottles: int, numExchange: int) -> int:
        b_drunk = numBottles
        b_empty = numBottles
        while b_empty >= numExchange:
            b_drunk += 1
            b_empty -= numExchange - 1
            numExchange += 1
        return b_drunk


s = Solution()
print(s.maxBottlesDrunk(numBottles=13, numExchange=6))
print(s.maxBottlesDrunk(numBottles=10, numExchange=3))
print(s.maxBottlesDrunk2(numBottles=13, numExchange=6))
print(s.maxBottlesDrunk2(numBottles=10, numExchange=3))
