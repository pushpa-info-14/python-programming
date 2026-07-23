class Solution:
    def punishmentNumber(self, n: int) -> int:

        def find_partition(num, target):
            s = str(num)
            length = len(s)

            for bit_mask in range(1 << length):
                total = 0
                t = ""
                for i in range(length):
                    t += s[i]
                    if bit_mask & 1 << i:
                        total += int(t)
                        t = ""
                if len(t):
                    total += int(t)
                if total == target:
                    return True
            return False

        res = 0
        for i in range(n + 1):
            p = i * i

            if find_partition(p, i):
                res += p
        return res

    def punishmentNumber2(self, n: int) -> int:

        def find_partition(num, target):
            if target < 0 or num < target:
                return False
            if num == target:
                return True
            return (
                    find_partition(num // 10, target - num % 10) or
                    find_partition(num // 100, target - num % 100) or
                    find_partition(num // 1000, target - num % 1000)
            )

        res = 0
        for i in range(n + 1):
            p = i * i

            if find_partition(p, i):
                res += p
        return res


s = Solution()
print(s.punishmentNumber(10))
print(s.punishmentNumber(37))

print(s.punishmentNumber2(10))
print(s.punishmentNumber2(37))
