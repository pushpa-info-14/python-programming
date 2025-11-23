class Solution:
    def reverseVowels(self, s: str) -> str:
        result = list(s)
        vowels = list("aeiouAEIOU")

        l, r = 0, len(s) - 1

        while l < r:
            while l < r and s[l] not in vowels:
                l += 1
            while l < r and s[r] not in vowels:
                r -= 1

            result[l], result[r] = result[r], result[l]
            l += 1
            r -= 1

        return "".join(result)


s = Solution()
print(s.reverseVowels("IceCreAm"))
