from collections import defaultdict


def to_base(n, k):
    res = []
    while n:
        res.append(str(n % k))
        n //= k
    return res


def is_prime(digits):
    number = "".join(digits)
    return number == number[::-1]


cache = defaultdict(list)


# for k in range(2, 10):
#     target = 0
#     for i in range(1, 10 ** 9):
#         if is_prime(to_base(i, 10)) and is_prime(to_base(i, k)):
#             target += 1
#             cache[k].append(i)
#             print(k, target)
#             if target == 30:
#                 break


class Solution:
    def kMirror(self, k: int, n: int) -> int:
        return sum(cache[k][:n])

    def kMirror2(self, k: int, n: int) -> int:
        def isPalindrome(x: int) -> bool:
            digit = list()
            while x:
                digit.append(x % k)
                x //= k
            return digit == digit[::-1]

        left, cnt, ans = 1, 0, 0
        while cnt < n:
            right = left * 10
            # op = 0 indicates enumerating odd-length palindromes
            # op = 1 indicates enumerating even-length palindromes
            for op in [0, 1]:
                # enumerate i'
                for i in range(left, right):
                    if cnt == n:
                        break

                    combined = i
                    x = i // 10 if op == 0 else i
                    while x:
                        combined = combined * 10 + x % 10
                        x //= 10
                    if isPalindrome(combined):
                        cnt += 1
                        ans += combined
            left = right

        return ans


s = Solution()
# print(s.kMirror(k=2, n=5))
# print(s.kMirror(k=3, n=7))
# print(s.kMirror(k=7, n=17))
print(s.kMirror2(k=2, n=5))
print(s.kMirror2(k=3, n=7))
print(s.kMirror2(k=7, n=17))
