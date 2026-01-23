from typing import List


class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        n = len(score)
        score_to_index = {}
        for i in range(len(score)):
            score_to_index[score[i]] = i

        score.sort(reverse=True)
        ranks = {
            0: "Gold Medal",
            1: "Silver Medal",
            2: "Bronze Medal"
        }

        res = [""] * n
        for i in range(n):
            if i in ranks:
                res[score_to_index[score[i]]] = ranks[i]
            else:
                res[score_to_index[score[i]]] = str(i + 1)

        return res


s = Solution()
print(s.findRelativeRanks(score=[5, 4, 3, 2, 1]))
print(s.findRelativeRanks(score=[10, 3, 8, 9, 4]))
