class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        powers = set()
        p = 1
        for i in range(31):
            powers.add(''.join(sorted(list(str(p << i)))))

        return ''.join(sorted(list(str(n)))) in powers


s = Solution()
print(s.reorderedPowerOf2(1))
print(s.reorderedPowerOf2(10))
print(s.reorderedPowerOf2(16))
