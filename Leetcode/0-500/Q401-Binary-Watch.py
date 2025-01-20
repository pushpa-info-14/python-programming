from typing import List


class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:

        res = []
        for i in range(1024):
            bit_count = 0
            n = i
            while n:
                n= n & (n - 1)
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

s = Solution()
print(s.readBinaryWatch(1))
print(s.readBinaryWatch(2))
print(s.readBinaryWatch(9))