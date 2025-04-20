def countDigitSum(num):
    summation = 0
    while num:
        summation += num % 10
        num //= 10
    return summation


class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        count = 0
        while low <= high:
            str_num = str(low)
            str_len = len(str_num)
            if str_len % 2 == 0:
                part1 = str_num[:str_len // 2]
                part2 = str_num[str_len // 2:]
                if countDigitSum(int(part1)) == countDigitSum(int(part2)):
                    count += 1
            low += 1
        return count


s = Solution()
print(s.countSymmetricIntegers(1, 100))
print(s.countSymmetricIntegers(1200, 1230))
