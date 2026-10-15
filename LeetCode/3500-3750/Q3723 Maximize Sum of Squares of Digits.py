class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        res = ''
        cur_sum = 0
        for i in range(num):
            digit = min(sum - cur_sum, 9)
            cur_sum += digit
            res += str(digit)
        return res if cur_sum == sum else ''

    def maxSumOfSquares2(self, num: int, sum: int) -> str:
        res = ''
        cur_sum = 0
        nines = sum // 9
        cur_sum += nines * 9
        res += '9' * nines
        if num < nines:
            return ""
        for i in range(num - nines):
            digit = min(sum - cur_sum, 9)
            cur_sum += digit
            res += str(digit)
        return res if cur_sum == sum else ''


s = Solution()
print(s.maxSumOfSquares(num=2, sum=3))
print(s.maxSumOfSquares(num=2, sum=17))
print(s.maxSumOfSquares(num=1, sum=10))
print('-----------------')
print(s.maxSumOfSquares2(num=2, sum=3))
print(s.maxSumOfSquares2(num=2, sum=17))
print(s.maxSumOfSquares2(num=1, sum=10))
