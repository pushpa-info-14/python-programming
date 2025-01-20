class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        for i in set(ransomNote):
            if ransomNote.count(i) > magazine.count(i):
                return False
        return True

s = Solution()
print(s.canConstruct("a", "b"))
print(s.canConstruct("aa", "ab"))
print(s.canConstruct("aa", "aab"))