from collections import defaultdict


class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        box_number = defaultdict(int)
        max_balls = 0
        for ball in range(lowLimit, highLimit + 1):
            digit_sum = 0
            while ball:
                digit_sum += ball % 10
                ball //= 10
            box_number[digit_sum] += 1
            max_balls = max(max_balls, box_number[digit_sum])
        return max_balls


s = Solution()
print(s.countBalls(lowLimit=1, highLimit=10))
print(s.countBalls(lowLimit=5, highLimit=15))
print(s.countBalls(lowLimit=19, highLimit=28))
