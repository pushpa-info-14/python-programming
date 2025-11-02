from typing import List


class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        res = [first]
        for i in range(len(encoded)):
            res.append(encoded[i] ^ res[i])
        return res


s = Solution()
print(s.decode(encoded=[1, 2, 3], first=1))
print(s.decode(encoded=[6, 2, 7, 3], first=4))
