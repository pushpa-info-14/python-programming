class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        chars = ["a", "b", "c"]
        happy_count = [0]
        res = [""]

        def backtracking(s):
            if happy_count[0] == k:
                return
            if len(s) == n:
                happy_count[0] += 1
                res[0] = s
                return
            for c in chars:
                if s[-1] != c:
                    backtracking(s + c)

        backtracking("a")
        backtracking("b")
        backtracking("c")
        return res[0] if happy_count[0] == k else ""


s = Solution()
print(s.getHappyString(1, 3))
print(s.getHappyString(1, 4))
print(s.getHappyString(3, 9))
