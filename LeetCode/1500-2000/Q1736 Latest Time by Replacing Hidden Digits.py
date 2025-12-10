class Solution:
    def maximumTime(self, time: str) -> str:
        t = list(time)
        if t[0] == '?':
            if t[1] in "?0123":
                t[0] = '2'
            else:
                t[0] = '1'
        if t[1] == '?':
            if t[0] == '2':
                t[1] = '3'
            else:
                t[1] = '9'
        if t[3] == '?':
            t[3] = '5'
        if t[4] == '?':
            t[4] = '9'
        return ''.join(t)


s = Solution()
print(s.maximumTime(time="2?:?0"))
print(s.maximumTime(time="0?:3?"))
print(s.maximumTime(time="1?:22"))
print(s.maximumTime(time="??:3?"))
