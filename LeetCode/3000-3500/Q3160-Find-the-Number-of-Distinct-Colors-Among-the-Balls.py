from typing import List


class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        index_to_color = {}
        color_to_cnt = {}

        res = []
        for index, color in queries:
            if index in index_to_color:
                color_to_cnt[index_to_color[index]] -= 1
                if color_to_cnt[index_to_color[index]] == 0:
                    del color_to_cnt[index_to_color[index]]

            if color not in color_to_cnt:
                color_to_cnt[color] = 1
            else:
                color_to_cnt[color] += 1
            index_to_color[index] = color

            res.append(len(color_to_cnt.keys()))

        return res


s = Solution()
print(s.queryResults(4, [[1, 4], [2, 5], [1, 3], [3, 4]]))
