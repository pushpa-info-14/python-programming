"""
Given a circular list of gas stations, where we can go from a station i to the station i + 1,
and the last one goes back to the first one. Find the index of the station from where we start
to be able to traverse all the stations and go back to the initial one without running out of gas.

Note that:
1. We can only move forward
2. The gas tank starts empty
3. gas[i] represents the amount of gas at the station i
4. cost[i] represents the cost to go from the station i to the next one
5. The answer is guaranteed to be unique
6. If the station we're searching for doesn't exist, return -1
"""


def can_traverse1(gas, cost, start):
    n = len(gas)
    remaining = 0
    i = start
    started = False
    while i != start or not started:
        started = True
        remaining += gas[i] - cost[i]
        if remaining < 0:
            return False
        i = (i + 1) % n
    return True


def gas_station1(gas, cost):
    for i in range(len(gas)):
        if can_traverse1(gas, cost, i):
            return i
    return -1


# T(n) = O(n2)
# S(n) = O(1)


"""
If a station start reaches a negative amount at the index i, then all stations between start and i
inclusive are invalid. We can start again from i + 1.
"""


def gas_station2(gas, cost):
    remaining = 0
    candidate = 0
    for i in range(len(gas)):
        remaining += gas[i] - cost[i]
        if remaining < 0:
            candidate = i + 1
            remaining = 0
    prev_remaining = sum(gas[:candidate]) - sum(cost[:candidate])
    if candidate == len(gas) or remaining + prev_remaining < 0:
        return -1
    else:
        return candidate
# T(n) = O(n)
# S(n) = O(1)


gas_test = [1, 5, 3, 3, 5, 3, 1, 3, 4, 5]
cost_test = [5, 2, 2, 8, 2, 4, 2, 5, 1, 2]
print(gas_station1(gas_test, cost_test))
print(gas_station2(gas_test, cost_test))
