class Solution:
    def kthCharacter(self, k: int) -> str:
        word = 'a'
        while len(word) < k:
            w = ''
            for c in word:
                w += chr(ord('a') + (ord(c) + 1 - ord('a')) % 26)
            word += w
        return word[k - 1]

    def kthCharacter2(self, k: int) -> str:
        word = [0]
        while len(word) < k:
            w = [i + 1 for i in word]
            word = word + w
        return chr(word[k - 1] % 26 + ord('a'))


s = Solution()
print(s.kthCharacter(5))
print(s.kthCharacter(10))
print(s.kthCharacter2(5))
print(s.kthCharacter2(10))
