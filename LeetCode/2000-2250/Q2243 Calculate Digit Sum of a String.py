class Solution:
    def digitSum(self, s: str, k: int) -> str:
        def process(digits):
            n = len(digits)
            new_digits = []
            i = 0
            while i < n:
                cur = 0
                for _ in range(i, min(i + k, n)):
                    cur += int(digits[i])
                    i += 1
                for c in str(cur):
                    new_digits.append(c)
            return new_digits

        res = [c for c in s]
        while len(res) > k:
            res = process(res)

        return "".join(res)


s = Solution()
print(s.digitSum(s="11111222223", k=3))
print(s.digitSum(s="00000000", k=3))
print(s.digitSum(s="01234567890", k=2))
