class Solution:
    def countDigitOccurrences(self, nums: list[int], digit: int) -> int:
        res = 0
        for num in nums:
            while num:
                if num % 10 == digit:
                    res += 1
                num //= 10
        return res


s = Solution()
print(s.countDigitOccurrences(nums=[12, 54, 32, 22], digit=2))
print(s.countDigitOccurrences(nums=[1, 34, 7], digit=9))
