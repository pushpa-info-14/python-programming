class Solution:
    def intToRoman(self, num: int) -> str:
        nums = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        strings = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        ans = ""
        for i in range(len(nums)):
            while num >= nums[i]:
                ans += strings[i]
                num -= nums[i]
        return ans


s = Solution()
print(s.intToRoman(7))
print(s.intToRoman(10))
print(s.intToRoman(11))
print(s.intToRoman(3749))
print(s.intToRoman(58))
print(s.intToRoman(1994))
