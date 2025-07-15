class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False
        if not word.isalnum():
            return False
        include_vowels = False
        include_consonant = False
        vowels = "aeiouAEIOU"
        for c in word:
            if c in vowels:
                include_vowels = True
                break
        for c in word:
            if c not in vowels and c.isalpha():
                include_consonant = True
                break
        return include_vowels and include_consonant

    def isValid2(self, word: str) -> bool:
        return (
                len(word) >= 3
                and all(char.isalnum() for char in word)
                and any(char.lower() in "aeiou" for char in word)
                and any(char.isalpha() and char.lower() not in "aeiou" for char in word)
        )


s = Solution()
print(s.isValid(word="234Adas"))
print(s.isValid(word="b3"))
print(s.isValid(word="a3$e"))
print(s.isValid(word="UuE6"))
print(s.isValid2(word="234Adas"))
print(s.isValid2(word="b3"))
print(s.isValid2(word="a3$e"))
print(s.isValid2(word="UuE6"))
