import math

def to_decimal(val, precision = 2):
    fact = 1000 * 10 ** precision
    return math.floor(val * fact) / fact

class ValveShimCalculator:
    def __init__(self, readings, c_spec):
        self._readings = readings
        self._c_spec = c_spec

    def t_new(self, t_old, c_measured):
        return t_old + (c_measured - self._c_spec)

    def cal(self, ceil_to_even=False):
        values = []
        for c_measured, t_old in self._readings:
            t = math.ceil(self.t_new(t_old, c_measured) * 100)
            if ceil_to_even:
                t += t % 2
            values.append(t / 100)
        return values


intake_readings = [
    [0.28, 2.63],
    [0.28, 2.63],
    [0.35, 2.63],
    [0.35, 2.51],
    [0.38, 2.59],
    [0.38, 2.61],
    [0.38, 2.56],
    [0.38, 2.56]
]
exhaust_readings = [
    [0.40, 2.54],
    [0.40, 2.44],
    [0.40, 2.53],
    [0.40, 2.46],
    [0.40, 2.46],
    [0.40, 2.41],
    [0.48, 2.52],
    [0.48, 2.47]
]
intake = ValveShimCalculator(intake_readings, 0.30)  #      0.32 - 0.40 HOT, 0.25 - 0.33 COLD
exhaust = ValveShimCalculator(exhaust_readings, 0.35)  #    0.37 - 0.45 HOT, 0.32 - 0.40 COLD
res1 = intake.cal(True)
res2 = exhaust.cal(True)
res = res1 + res2
res.sort()
print("Intake :", res1)
print("Exhaust:", res2)
print("Sorted Req :", res)

ext1 = [i[1] for i in intake_readings]
ext2 = [i[1] for i in exhaust_readings]
ext = ext1 + ext2
ext.sort()
for i in range(len(ext)):
    temp = math.ceil(ext[i] * 100)
    temp += temp % 2
    ext[i] = temp / 100
print("Sorted Ext :", ext)

matching = []
required = []

n = len(res)
for i in range(n):
    found = False
    for j in range(n):
        if res[i] == ext[j]:
            matching.append(res[i])
            ext[j] = 0
            found = True
            break
    if not found:
        required.append(res[i])
ext = [shim for shim in ext if shim != 0]
print("Matching:", matching)
print("Required:", required)
print("Not used:", ext)

gap = []
for i in range(len(required)):
    gap.append(to_decimal(required[i] - ext[i]))
    # gap.append(required[i] - ext[i])
print("Gap     :", gap)