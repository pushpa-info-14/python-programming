class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        n = len(word)

        if numFriends == 1:
            return word

        window_size = n - numFriends + 1
        result = ""
        for i in range(n):
            if result < word[i:i + window_size]:
                result = word[i:i + window_size]

        return result


s = Solution()
print(s.answerString(word="dbca", numFriends=2))
print(s.answerString(word="gggg", numFriends=4))
print(s.answerString(word="aann", numFriends=2))
print(s.answerString(word="gh", numFriends=1))
