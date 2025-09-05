class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        """
        num1 = (pow(2, i) + num2) // sample
        num1 - m*num2 = pow(2, i1) + pow(2, i2) + ... + pow(2, im)

        0 <= im <= 60

        pow(2, i1) + pow(2, i2) + ... + pow(2, im) we can make any number using this

        its possible only if
        num1 - m*num2 >= 0
        num1 >= m*num2

        we have to just find m such that
        num1 >= m*num2 and num1 - m*num2 = value has it least m bit because to make any number we need to have diff between those to has same bit count
        """
        for m in range(1, 61):
            x = num1 - num2 * m
            if x < m:
                return -1
            if m >= x.bit_count():
                return m
        return -1


s = Solution()
print(s.makeTheIntegerZero(num1=3, num2=-2))
print(s.makeTheIntegerZero(num1=5, num2=7))
