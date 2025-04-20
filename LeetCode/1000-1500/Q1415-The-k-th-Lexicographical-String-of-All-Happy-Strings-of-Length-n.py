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

    def getHappyString2(self, n: int, k: int) -> str:
        total_happy = 3 * 2 ** (n - 1)

        res = []
        choices = "abc"
        left, right = 1, total_happy

        for i in range(n):
            cur = left
            partition_size = (right - left + 1) // len(choices)
            # Polling: 1 - 4, 5 - 8, 9 - 12

            for c in choices:
                # cur <= k < cur + partition_size
                if k in range(cur, cur + partition_size):
                    res.append(c)
                    left = cur
                    right = cur + partition_size - 1
                    choices = "abc".replace(c, "")
                    break
                cur += partition_size
        return "".join(res)


s = Solution()
print(s.getHappyString(1, 3))
print(s.getHappyString(1, 4))
print(s.getHappyString(3, 9))

print(s.getHappyString2(1, 3))
print(s.getHappyString2(1, 4))
print(s.getHappyString2(3, 9))
