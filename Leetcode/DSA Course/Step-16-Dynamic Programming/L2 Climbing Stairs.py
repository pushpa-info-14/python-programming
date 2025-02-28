# 1. Try to represent the problem in terms of indexes
# 2. Do all possible stuffs on that index according to the problem statement
# 3. Sum of all stuffs -> Count all the ways
#    Min of all stuffs -> Find min...
#    Max of all stuffs -> Find max...

def climb(n, dp=None):
    if dp is None:
        dp = {}
    if n == 0: return 0
    if n == 1: return 1

    if n in dp:
        return dp[n]

    dp[n] = climb(n - 2, dp) + climb(n - 1, dp)
    return dp[n]

print(climb(2))
print(climb(5))
print(climb(10))
print(climb(1000))