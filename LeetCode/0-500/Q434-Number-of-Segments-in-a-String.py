class Solution:
    def countSegments(self, s: str) -> int:
        splits = s.split(" ")
        cnt = 0
        for i in splits:
            if i != "":
                cnt += 1
        return cnt


s = Solution()
print(s.countSegments("He llo   "))
