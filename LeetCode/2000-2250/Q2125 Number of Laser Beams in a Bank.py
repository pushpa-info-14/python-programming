from typing import List


class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        res = 0
        prev = 0
        for row in bank:
            devices = row.count('1')
            res += prev * devices
            if devices:
                prev = devices
        return res


s = Solution()
print(s.numberOfBeams(bank=["011001", "000000", "010100", "001000"]))
print(s.numberOfBeams(bank=["000", "111", "000"]))
