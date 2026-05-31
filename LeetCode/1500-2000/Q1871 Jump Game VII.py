import bisect


class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        prev = [0]
        for i in range(1, n):
            if s[i] == '1':
                continue
            j = bisect.bisect_right(prev, i - minJump)
            if j > 0 and i <= prev[j - 1] + maxJump:
                prev.append(i)
        return prev[-1] == n - 1

    def canReach2(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        if s[-1] == '1':
            return False
        diff = [0] * (n + maxJump + 1)
        diff[minJump] += 1
        diff[maxJump + 1] -= 1
        for i in range(1, n):
            diff[i] += diff[i - 1]
            if s[i] == '1' or diff[i] == 0:
                continue
            diff[i + minJump] += 1
            diff[i + maxJump + 1] -= 1
        return diff[n - 1] > 0


s = Solution()
print(s.canReach(s="001010", minJump=2, maxJump=3))
print(s.canReach(s="011010", minJump=2, maxJump=3))
print(s.canReach(s="01101110", minJump=2, maxJump=3))
print('-------------')
print(s.canReach2(s="001010", minJump=2, maxJump=3))
print(s.canReach2(s="011010", minJump=2, maxJump=3))
print(s.canReach2(s="01101110", minJump=2, maxJump=3))
