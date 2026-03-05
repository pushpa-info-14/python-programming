class Solution:
    def minOperations(self, s: str, k: int) -> int:
        n = len(s)
        zeros = s.count("0")
        ones = n - zeros
        if zeros == 0:
            return 0
        for op in range(1, n + 1):
            flips = op * k
            if (flips - zeros) % 2 == 1:
                continue
            if op % 2 == 0:
                if zeros <= flips <= zeros * (op - 1) + ones * op:
                    return op
            else:
                if zeros <= flips <= zeros * op + ones * (op - 1):
                    return op
        return -1


s = Solution()
print(s.minOperations(s="110", k=1))
print(s.minOperations(s="0101", k=3))
print(s.minOperations(s="101", k=2))
