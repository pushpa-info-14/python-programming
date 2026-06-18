class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        hour_hand = (hour * 5 + 5 * (minutes / 60)) % 60
        diff = abs(hour_hand - minutes)
        angle = diff * 360 / 60
        return min(angle, 360 - angle)


s = Solution()
print(s.angleClock(hour=12, minutes=30))
print(s.angleClock(hour=3, minutes=30))
print(s.angleClock(hour=3, minutes=15))
print(s.angleClock(hour=1, minutes=57))
