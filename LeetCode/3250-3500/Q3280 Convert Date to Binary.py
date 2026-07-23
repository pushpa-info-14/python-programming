def to_binary(num):
    res = ''
    while num:
        res = str(num % 2) + res
        num //= 2
    return res


class Solution:
    def convertDateToBinary(self, date: str) -> str:
        splits = date.split('-')
        year = int(splits[0])
        month = int(splits[1])
        day = int(splits[2])
        return f"{to_binary(year)}-{to_binary(month)}-{to_binary(day)}"


s = Solution()
print(s.convertDateToBinary(date="2080-02-29"))
print(s.convertDateToBinary(date="1900-01-01"))
