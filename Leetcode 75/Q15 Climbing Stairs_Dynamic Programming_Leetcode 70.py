"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:
    Input: n = 2
    Output: 2
    Explanation: There are two ways to climb to the top.
        1. 1 step + 1 step
        2. 2 steps

Example 2:
    Input: n = 3
    Output: 3
    Explanation: There are three ways to climb to the top.
        1. 1 step + 1 step + 1 step
        2. 1 step + 2 steps
        3. 2 steps + 1 step

Draw a decision tree to understand

| 0 | 1 | 2 | 3 | 4 | 5 |
-------------------------
| 8 | 5 | 3 | 2 | 1 | 1 |
"""


def climb_stairs(n):
    one, two = 1, 1

    for i in range(n - 1):
        two, one = one, one + two
    return one


print(climb_stairs(1))
print(climb_stairs(2))
print(climb_stairs(3))
print(climb_stairs(4))
print(climb_stairs(5))
print(climb_stairs(6))
