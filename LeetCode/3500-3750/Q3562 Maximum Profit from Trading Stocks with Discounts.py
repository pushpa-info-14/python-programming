from typing import List


class Solution:
    def maxProfit(self, n: int, present: List[int], future: List[int], hierarchy: List[List[int]], budget: int) -> int:
        adj_list = [[] for _ in range(n)]
        for e in hierarchy:
            adj_list[e[0] - 1].append(e[1] - 1)

        def dfs(u: int):
            cost = present[u]
            d_cost = present[u] // 2

            # dp[u][state][budget]
            # state = 0: Do not purchase parent node, state = 1: Must purchase parent node
            dp0 = [0] * (budget + 1)
            dp1 = [0] * (budget + 1)

            # sub_profit[state][budget]
            # state = 0: discount not available, state = 1: discount available
            sub_profit0 = [0] * (budget + 1)
            sub_profit1 = [0] * (budget + 1)
            u_size = cost

            for v in adj_list[u]:
                child_dp0, child_dp1, v_size = dfs(v)
                u_size += v_size
                for i in range(budget, -1, -1):
                    for sub in range(min(v_size, i) + 1):
                        if i - sub >= 0:
                            sub_profit0[i] = max(sub_profit0[i], sub_profit0[i - sub] + child_dp0[sub])
                            sub_profit1[i] = max(sub_profit1[i], sub_profit1[i - sub] + child_dp1[sub])

            for i in range(budget + 1):
                dp0[i] = sub_profit0[i]
                dp1[i] = sub_profit0[i]
                if i >= d_cost:
                    dp1[i] = max(sub_profit0[i], sub_profit1[i - d_cost] + future[u] - d_cost)
                if i >= cost:
                    dp0[i] = max(sub_profit0[i], sub_profit1[i - cost] + future[u] - cost)

            return dp0, dp1, u_size

        return dfs(0)[0][budget]


s = Solution()
print(s.maxProfit(n=2, present=[1, 2], future=[4, 3], hierarchy=[[1, 2]], budget=3))  # 5
print(s.maxProfit(n=2, present=[3, 4], future=[5, 8], hierarchy=[[1, 2]], budget=4))  # 4
print(s.maxProfit(n=3, present=[4, 6, 8], future=[7, 9, 11], hierarchy=[[1, 2], [1, 3]], budget=10))  # 10
print(s.maxProfit(n=3, present=[5, 2, 3], future=[8, 5, 6], hierarchy=[[1, 2], [2, 3]], budget=7))  # 12
