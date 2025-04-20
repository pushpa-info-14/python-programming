# Similar to backtracking
# Uses state based tree
# Used to solve optimization problems and minimization problems
# We can convert to maximization problem into minimization and solve it also
#
# Using Queue - FIFO Branch and Bound
# Using Stack - LIFO Branch and Bound
# Least Cost Branch and Bound
from typing import List

# u = Sum of all penalties except that included in solution
# c = Sum of penalties till the last job considered

def job_sequencing(jobs:List[str], penalty:List[int], deadline:List[int], time:List[int]):

    print("")

jobs = ["J1", "J2", "J3", "J4"]
penalty = [5, 10, 6, 3]  # To maximize the profit, penalty should be minimized
deadline = [1, 3, 2, 1]
time = [1, 2, 1, 1]

print(job_sequencing(jobs, penalty, deadline, time))
