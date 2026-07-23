class Solution:
    def sortVowels(self, s: str) -> str:
        s_array = list(s)
        vowels = 'aeiouAEIOU'
        s_vowels = []
        for c in s_array:
            if c in vowels:
                s_vowels.append(c)
        s_vowels.sort()
        i = 0
        for idx, c in enumerate(s_array):
            if c in vowels:
                s_array[idx] = s_vowels[i]
                i += 1
        return ''.join(s_array)


s = Solution()
print(s.sortVowels(s="lEetcOde"))
print(s.sortVowels(s="lYmpH"))
