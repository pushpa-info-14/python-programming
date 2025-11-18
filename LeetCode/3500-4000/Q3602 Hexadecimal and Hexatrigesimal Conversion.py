class Solution:
    def concatHex36(self, n: int) -> str:
        digit_map = []
        for x in range(10):
            digit_map.append(str(x))
        for c in range(ord('A'), ord('Z') + 1):
            digit_map.append(chr(c))

        def convert_to_base(num, base):
            res = ''
            while num:
                res += digit_map[num % base]
                num //= base
            return res[::-1]

        return convert_to_base(n * n, 16) + convert_to_base(n * n * n, 36)


s = Solution()
print(s.concatHex36(13))
print(s.concatHex36(36))
