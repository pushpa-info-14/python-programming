class Solution:
    def intToRoman(self, num: int) -> str:
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
