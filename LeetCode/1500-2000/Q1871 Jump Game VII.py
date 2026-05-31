import bisect


class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        prev = [0]
        for i in range(1, n):
            if s[i] == '1':
                continue
            j = bisect.bisect_right(prev, i - minJump)
            if j and i <= prev[j - 1] + maxJump:
                prev.append(i)
        return prev[-1] == n - 1


s = Solution()
print(s.canReach(s="011010", minJump=2, maxJump=3))
print(s.canReach(s="01101110", minJump=2, maxJump=3))
