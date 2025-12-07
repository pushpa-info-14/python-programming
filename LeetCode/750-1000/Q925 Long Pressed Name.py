class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i, j = 0, 0
        while j < len(typed):
            if i < len(name) and name[i] == typed[j]:
                i += 1
            elif j == 0 or typed[j] != typed[j - 1]:
                return False
            j += 1
        return len(name) == i


s = Solution()
print(s.isLongPressedName(name="alex", typed="aaleex"))
print(s.isLongPressedName(name="saeed", typed="ssaaedd"))
print(s.isLongPressedName(name="alex", typed="aaleexa"))
