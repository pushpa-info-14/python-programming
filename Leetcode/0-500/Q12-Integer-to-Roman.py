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

    def intToRoman2(self, num: int) -> str:
        mapping = {
            1: "I",
            4: "IV",
            5: "V",
            9: "IX",
            10: "X",
            40: "XL",
            50: "L",
            90: "XC",
            100: "C",
            400: "CD",
            500: "D",
            900: "CM",
            1000: "M"
        }

        values = sorted(mapping.keys(), reverse= True)

        res = ""
        for i in values:
            if num // i:
                res += mapping[i] * (num // i)
                num = num % i
        return res

s = Solution()
print(s.intToRoman(7))
print(s.intToRoman(10))
print(s.intToRoman(11))
print(s.intToRoman(3749))
print(s.intToRoman(58))
print(s.intToRoman(1994))
print(s.intToRoman2(7))
print(s.intToRoman2(10))
print(s.intToRoman2(11))
print(s.intToRoman2(3749))
print(s.intToRoman2(58))
print(s.intToRoman2(1994))
