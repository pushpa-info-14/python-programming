class Fancy:
    mod = 10 ** 9 + 7

    def __init__(self):
        self.seq = []
        self.add = 0
        self.mul = 1

    def append(self, val: int) -> None:
        self.seq.append((val - self.add) * pow(self.mul, -1, self.mod) % self.mod)

    def addAll(self, inc: int) -> None:
        self.add += inc

    def multAll(self, m: int) -> None:
        self.mul = (self.mul * m) % self.mod
        self.add = (self.add * m) % self.mod

    def getIndex(self, idx: int) -> int:
        if idx >= len(self.seq):
            return -1
        return (self.seq[idx] * self.mul + self.add) % self.mod


"""
n = b * m + s

n = actual number
b = base number
m = accumulated multiplier
s = accumulated sum

We store the base in the sequence

b = (n - s) / m % mod
b = (n - s) * m¯¹
"""
fancy = Fancy()
fancy.append(2)
fancy.addAll(3)
fancy.append(7)
fancy.multAll(2)
print(fancy.getIndex(0))
fancy.addAll(3)
fancy.append(10)
fancy.multAll(2)
print(fancy.getIndex(0))
print(fancy.getIndex(1))
print(fancy.getIndex(2))
