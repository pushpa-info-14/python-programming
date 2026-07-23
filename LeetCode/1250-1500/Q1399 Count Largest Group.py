from collections import defaultdict


class Solution:
    def countLargestGroup(self, n: int) -> int:
        freq = defaultdict(int)

        for num in range(1, n + 1):
            digit_count = 0
            while num > 0:
                digit_count += num % 10
                num = num // 10
            freq[digit_count] += 1
        max_freq = max(freq.values())
        res = 0
        for num in freq.values():
            if num == max_freq:
                res += 1
        return res


s = Solution()
print(s.countLargestGroup(13))
print(s.countLargestGroup(2))
