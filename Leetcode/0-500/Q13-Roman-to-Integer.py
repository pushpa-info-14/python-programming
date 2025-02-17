class Solution:
    def romanToInt(self, s: str) -> int:

        dist = {
            "I": 1,
            "IV": 4,
            "V": 5,
            "IX": 9,
            "X": 10,
            "XL": 40,
            "L": 50,
            "XC": 90,
            "C": 100,
            "CD": 400,
            "D": 500,
            "CM": 900,
            "M": 1000
        }

        n = len(s)
        res = 0
        i = 0
        while i < n:
            if i + 1 < n and s[i:i + 2] in dist:
                res += dist[s[i:i + 2]]
                i += 2
            else:
                res += dist[s[i]]
                i += 1
        return res


s = Solution()
print(s.romanToInt("III"))
print(s.romanToInt("LVIII"))
print(s.romanToInt("MCMXCIV"))
