from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res = []
        for i in range(1, n + 1):
            is_divisible_by_3 = i % 3 == 0
            is_divisible_by_5 = i % 5 == 0
            if is_divisible_by_3 and is_divisible_by_5:
                res.append("FizzBuzz")
            elif is_divisible_by_3:
                res.append("Fizz")
            elif is_divisible_by_5:
                res.append("Buzz")
            else:
                res.append(str(i))
        return res


s = Solution()
print(s.fizzBuzz(3))
print(s.fizzBuzz(5))
print(s.fizzBuzz(15))
