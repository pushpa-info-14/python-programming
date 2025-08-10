class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        powers = set()
        p = 1
        for i in range(31):
            powers.add(''.join(sorted(list(str(p << i)))))

        return ''.join(sorted(list(str(n)))) in powers

    def reorderedPowerOf22(self, n: int) -> bool:
        sorted_n = ''.join(sorted(list(str(n))))
        for i in range(31):
            if ''.join(sorted(list(str(1 << i)))) == sorted_n:
                return True
        return False


s = Solution()
print(s.reorderedPowerOf2(1))
print(s.reorderedPowerOf2(10))
print(s.reorderedPowerOf2(16))
print(s.reorderedPowerOf22(1))
print(s.reorderedPowerOf22(10))
print(s.reorderedPowerOf22(16))
