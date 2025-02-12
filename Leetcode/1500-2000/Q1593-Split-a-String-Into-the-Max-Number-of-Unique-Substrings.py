class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        n = len(s)
        res = [0]
        substrings = set()

        def dfs(cur):
            if cur == "":
                res[0] = max(res[0], len(substrings))
                return

            for j in range(1, len(cur) + 1):
                new_s = cur[:j]
                if new_s not in substrings:
                    substrings.add(new_s)
                    dfs(cur[j:])
                    substrings.remove(new_s)

        dfs(s)
        return res[0]


s = Solution()
print(s.maxUniqueSplit("ababccc"))
print(s.maxUniqueSplit("aba"))
print(s.maxUniqueSplit("aa"))
print(s.maxUniqueSplit("wwwzfvedwfvhsww"))
