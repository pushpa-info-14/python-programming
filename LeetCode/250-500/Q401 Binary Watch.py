from typing import List


class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        res = []
        for i in range(1024):
            bit_count = 0
            n = i
            while n:
                n = n & (n - 1)
                bit_count += 1
            if bit_count != turnedOn:
                continue

            h = i >> 6
            m = i % 64
            if h < 12 and m < 60:
                if m < 10:
                    t = str(h) + ":0" + str(m)
                else:
                    t = str(h) + ":" + str(m)
                res.append(t)
        return res

    def readBinaryWatch2(self, turnedOn: int) -> List[str]:
        res = []
        for h in range(12):
            for m in range(60):
                if h.bit_count() + m.bit_count() == turnedOn:
                    t = str(h) + ":"
                    t += "0" + str(m) if m < 10 else str(m)
                    res.append(t)
        return res


s = Solution()
print(s.readBinaryWatch(1))
print(s.readBinaryWatch(2))
print(s.readBinaryWatch(9))
print("----------------")
print(s.readBinaryWatch2(1))
print(s.readBinaryWatch2(2))
print(s.readBinaryWatch2(9))
