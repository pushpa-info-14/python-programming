from typing import List


class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        n = len(words)
        indexes = []
        for i in range(n):
            if words[i] == target:
                indexes.append(i)
        if len(indexes) == 0:
            return -1
        res = n
        for i in indexes:
            d = abs(startIndex - i)
            res = min(res, d, n - d)
        return res


s = Solution()
print(s.closestTarget(words=["hello", "i", "am", "leetcode", "hello"], target="hello", startIndex=1))
print(s.closestTarget(words=["a", "b", "leetcode"], target="leetcode", startIndex=0))
print(s.closestTarget(words=["i", "eat", "leetcode"], target="ate", startIndex=0))
print(s.closestTarget(
    words=["hsdqinnoha", "mqhskgeqzr", "zemkwvqrww", "zemkwvqrww", "daljcrktje", "fghofclnwp", "djwdworyka",
           "cxfpybanhd", "fghofclnwp", "fghofclnwp"], target="zemkwvqrww", startIndex=8))
