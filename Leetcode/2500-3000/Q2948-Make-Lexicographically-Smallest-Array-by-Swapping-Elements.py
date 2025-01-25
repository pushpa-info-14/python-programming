from collections import deque
from typing import List

# 1. Don't need to worry about digits for lexicographically
# 2. Greedy?
# 3. Custom sorting?
# 4. Are new swaps possible after previous swaps?
#   Kinda, [3, 2, 1] limit = 1
#   Can't be greedy? Maybe greedy + scan elements in between
#   Since above all have abs diff <= limit, all swappable

#   [5, 3, 2, 1] limit = 1
#   Here 5 is stuck

#   [6, 5, 3, 2, 1] limit = 1
#   Here, 6 and 5 can be sorted, but separately from 3,2,1

#   [6, 3, 5, 2, 1] limit = 1
#   Here, same thing, except sections are non-contiguous

class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:

        groups = [] # list of queues
        num_to_group = {} # nums[i] -> groups index

        for num in sorted(nums):
            if not groups or abs(num - groups[-1][-1]) > limit:
                groups.append(deque())
            groups[-1].append(num)
            num_to_group[num] = len(groups) - 1

        res = []
        for num in nums:
            j = num_to_group[num]
            res.append(groups[j].popleft())
        return res

s = Solution()
print(s.lexicographicallySmallestArray([1,5,3,9,8], 2))
print(s.lexicographicallySmallestArray([1,7,6,18,2,1], 3))
print(s.lexicographicallySmallestArray([1,7,28,19,10],3))
