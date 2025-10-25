from collections import Counter
from itertools import permutations

all_perms = []
for i in range(1, 8):
    curr_list = [i] * i
    curr_perms = list(set(permutations(curr_list)))
    all_perms.extend(curr_perms)
    if i == 1:
        curr_list = [1, 2, 2, 3, 3, 3]
        curr_perms = list(set(permutations(curr_list)))
        all_perms.extend(curr_perms)
        curr_list = [1, 2, 2, 4, 4, 4, 4]
        curr_perms = list(set(permutations(curr_list)))
        all_perms.extend(curr_perms)
    for j in range(1, i // 2 + 1):
        a, b = j, i - j
        if a == b:
            break
        curr_list = [a] * a + [b] * b
        curr_perms = list(set(permutations(curr_list)))
        all_perms.extend(curr_perms)
all_perms = [int(''.join(str(a) for a in num)) for num in all_perms]
all_perms.sort()


class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        max_val = 1224444
        for i in range(n + 1, max_val):
            freq = Counter(str(i))
            is_valid = True
            for key, value in freq.items():
                if int(key) != value:
                    is_valid = False
                    break
            if is_valid:
                return i
        return max_val

    def nextBeautifulNumber2(self, n: int) -> int:
        for num in all_perms:
            if num > n:
                return num


s = Solution()
print(s.nextBeautifulNumber(1))
print(s.nextBeautifulNumber(1000))
print(s.nextBeautifulNumber(3000))
print(s.nextBeautifulNumber2(1))
print(s.nextBeautifulNumber2(1000))
print(s.nextBeautifulNumber2(3000))
