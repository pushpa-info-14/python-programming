class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        count = 0
        i = 0
        res = []

        for j, c in enumerate(s):
            if c == "1":
                count += 1
            else:
                count -= 1
            if count == 0:
                # We found a special substring s[i:j+1]
                # The middle part is s[i+1:j]
                # Recursively solve for the middle part
                middle_optimized = self.makeLargestSpecial(s[i + 1:j])
                res.append('1' + middle_optimized + '0')
                i = j + 1

        # Sort the components in descending order
        res.sort(reverse=True)
        return "".join(res)


s = Solution()
print(s.makeLargestSpecial(s="11011000"))
print(s.makeLargestSpecial(s="10"))
