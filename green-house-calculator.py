import math


class GreenHouseCalculator:
    def __init__(self, h, w):
        self._h = h
        self._w = w

    def radius(self):
        return (self._h ** 2 + self._w ** 2 / 4) / (2 * self._h)

    def central_angle(self):
        return 2 * math.asin(self._w / (2 * self.radius()))

    def arc_length(self):
        return self.radius() * self.central_angle()


cal = GreenHouseCalculator(3, 10)
print('R =', cal.radius())
print('Arc Length =', cal.arc_length())
