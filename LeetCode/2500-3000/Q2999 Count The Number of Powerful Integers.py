class Solution:
    MAX_DIGITS = 17

    def checkSubtract(self, num_str: str, num_digits: int, suffix: str, limit: int) -> bool:
        if num_digits < len(suffix):
            return False

        suffix_of_num = num_str[num_digits - len(suffix):]
        subtract = int(suffix_of_num) < int(suffix)

        if subtract:
            for i in range(num_digits - len(suffix)):
                if int(num_str[i]) > limit:
                    subtract = False
                    break
        return subtract

    def countValidNumbers(self, number_str: str, idx: int, max_digits: int,
                          is_tight: bool, limit: int, suffix: str, dp: list) -> int:
        if idx == max_digits:
            return 1
        if dp[idx][1 if is_tight else 0] != -1:
            return dp[idx][1 if is_tight else 0]

        suffix_len = len(suffix)

        if idx >= max_digits - suffix_len:
            suffix_idx = idx - (max_digits - suffix_len)
            low = high = int(suffix[suffix_idx])
        else:
            high = min(limit, int(number_str[idx])) if is_tight else limit
            low = 0

        total = 0
        for digit in range(low, high + 1):
            new_tight = is_tight and (digit == int(number_str[idx]))
            total += self.countValidNumbers(number_str, idx + 1, max_digits, new_tight, limit, suffix, dp)

        dp[idx][1 if is_tight else 0] = total
        return total

    def solveUpTo(self, num_str: str, num_digits: int, limit: int, suffix: str) -> int:
        dp = [[-1] * 2 for _ in range(self.MAX_DIGITS)]
        result = self.countValidNumbers(num_str, 0, num_digits, True, limit, suffix, dp)
        if self.checkSubtract(num_str, num_digits, suffix, limit):
            result -= 1
        return result

    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
        suffix_val = int(s)
        finish_str = str(finish)
        start_str = str(start - 1)

        finish_digits = len(finish_str)
        start_digits = len(start_str)

        upto_finish = self.solveUpTo(finish_str, finish_digits, limit, s) if finish >= suffix_val else 0
        upto_start = self.solveUpTo(start_str, start_digits, limit, s) if suffix_val < start else 0

        return upto_finish - upto_start


s = Solution()
print(s.numberOfPowerfulInt(start=1, finish=6000, limit=4, s="124"))
print(s.numberOfPowerfulInt(start=15, finish=215, limit=6, s="10"))
print(s.numberOfPowerfulInt(start=1000, finish=2000, limit=4, s="3000"))
