class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {}

        def dfs(cur, remainder):
            if len(cur) > 0:
                cur_num = int(cur)
                len_cur = len(cur)
                if len_cur == 1 and cur_num == 0:
                    return 0
                elif len_cur == 2:
                    if cur_num > 26 or cur_num < 10:
                        return 0

            if remainder == "":
                return 1
            if remainder in memo:
                return memo[remainder]
            res = 0
            if len(remainder) == 1:
                res += dfs(remainder[0], remainder[1:])
            else:
                res += dfs(remainder[0], remainder[1:])
                res += dfs(remainder[:2], remainder[2:])
            memo[remainder] = res
            return res

        return dfs("", s)


s = Solution()
print(s.numDecodings("12"))
print(s.numDecodings("226"))
print(s.numDecodings("06"))
print(s.numDecodings("111111111"))
print(s.numDecodings("111111111111111111111111111111111111111111111"))
