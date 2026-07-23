from typing import List


class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        return [celsius + 273.15, celsius * 1.80 + 32]


s = Solution()
print(s.convertTemperature(36.50))
print(s.convertTemperature(122.11))
