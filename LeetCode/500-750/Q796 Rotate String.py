class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        return len(s) == len(goal) and goal in (s + s)


s = Solution()
print(s.rotateString(s="abcde", goal="cdeab"))
print(s.rotateString(s="abcde", goal="abced"))
